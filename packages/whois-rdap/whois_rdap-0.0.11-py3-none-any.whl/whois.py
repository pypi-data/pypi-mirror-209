#!/usr/bin/env python3.8

#
# Imports
#

import os
import sys
from datetime import *
import csv
import re
import argparse
import requests
import random
import json
import ipaddress
import time
from collections import namedtuple

import py_helper as ph
from py_helper import DebugMode, CmdLineMode, ModuleMode, Msg, DbgMsg, ValidIP, IsNetwork

# Init Random
random.seed()

#
# Variables
#

# Version
VERSION=(0,0,11)
Version = __version__ = ".".join([ str(x) for x in VERSION ])

# Parser
__Parser__ = None

# Email Addess Expression
loose_emailaddr_exp = "(?P<username>[\w_-]+)@(?P<domain>([\w\-]+\.)+([\w\-]*))"

# Email Addess Expression
emailaddr_exp = r"^(?P<username>[\w_-]+)@(?P<domain>([\w\-]+\.)+([\w\-]*))$"
# Generic Abuse Email Expressions
abuse_exp = r"(?P<username>[\w_-]*abuse[^@]*)@(?P<domain>.+)"

# Cmd Line Header Strings
header = [ "http_result", "name","handle","start","end","cidr","parent","abuse" ]

# Helpers
WhoisResult = namedtuple("WhoisResult",['http_result','name','handle','start','end','cidr','parent','abuse','payload','country'])

# Whois ReSTful Web Service

# Whois RDAP
RDAP_URL="https://rdap-bootstrap.arin.net/bootstrap"

# Resources
ip = "/ip"
poc = "/poc"
org = "/org"
net = "/net"
asn = "/asn"
customer = "/customer"
rdns = "/rdns"

# Handles
orgs = "/orgs"
asns = "/asns"
nets = "/nets"
pocs = "/pocs"
parent = "/parent"
children = "/children"

# Global Pause Time In Seconds
PauseTime = 0

# Lookup Cache
LookupCache = None

#
# Lambdas
#

# Loose Email Check
mailcheck = lambda data: re.search(loose_emailaddr_exp,data)

# Check for occurrence of email address in string
#mailcheck = lambda data: re.search(emailaddr_exp,data)

# Check for user email with "abuse" in it
abusecheck = lambda data: re.search(abuse_exp,data)

#
# Classes
#

class CacheEntry:
	created = None
	expires = None
	key = None
	value = None

	def __init__(self,expires=None,key=None,value=None):
		"""Init Cache Entry"""

		if expires is not None:
			self.created = datetime.now()
			self.expires = datetime.now() + timedelta(seconds=expires)

		self.key = key
		self.value = value

	def read(self,reader):
		"""Read Cache Entry from Input"""

		row = reader.read()

		self.expires = datetime.fromtimestamp(float(row[1]))

		if self.expires > datetime.now():
			# finish reading
			self.created = datetime.fromtimestamp(float(row[0]))
			self.key = row[2]
			self.value = row[3]

	def write(self,writer):
		"""Write Cache Entry to Output"""

		if self.expires > datetime.now():
			row = [ self.created.timestamp(), self.expires.timestamp(), self.key, self.value ]

			writer.writerow(row)

class Cache:
	lookup = None
	items = None
	write_through = False
	backing_store = None
	default_ttl = 30

	def __init__(self,backingstore=None,writethrough=False,ttl=30):
		"""Initialize Instance of Cache"""

		self.items = list()
		self.lookup = dict()

		self.backing_store = backingstore
		self.write_through = writethrough
		if ttl is not None:
			self.default_ttl = ttl

	def Exists(self,key):
		"""Check if Key Exists In Cache"""

		result = None

		if key in self.lookup:
			result = self.lookup[key]

		return result

	def Save(self):
		"""Save Cache to Backing Store"""

		with open(self.backing_store,"w",newline='') as csvfile:
			writer = csv.writer(csvfile)

			for entry in self.items:
				entry.write(writer)

	def Load(self):
		"""Load Cache From Backing Store"""

		with open(self.backing_store,"r",newline='') as csvfile:
			reader = csv.reader(csvfile)

			entry = CacheEntry()

			entry.read(csvfile)

			self.lookup[key] = entry
			self.items.append(entry)

	def Append(self,item):
		"""Append new Cache Item To Backing Store"""

		with open(self.backing_store,"a",newline='') as csvfile:
			writer = csv.writer(csvfile)

			item.write(writer)

	def Change(self,key,value,expires=None):
		"""Change A Cache Item"""

		entry = self.lookup[key]

		if expires is None:
			expires = self.default_ttl

		if entry is not None:
			entry.value = value
			entry.expires = datetime.now() + timedelta(seconds=expires)

			if self.write_through and self.backing_store is not None:
				Save()

	def Add(self,key,value,expires=None):
		"""Add Item To Cache"""

		if expires is None:
			expires = self.default_ttl

		if not key in self.lookup:
			entry = CacheEntry(expires,key,value)

			self.lookup[key] = entry
			self.items.append(entry)

			if self.write_through and self.backing_store is not None:
				self.Append(entry)
		else:
			entry = self.lookup[key]

			if value != entry.value:
				self.Change(key,value)

	def Remove(self,key,writethrough=True):
		"""Clear Cache Entry"""

		if key in self.lookup:
			entry = self.lookup[key]

			del self.lookup[key]

			self.items.remove(entry)

			if writethrough and self.write_through and self.backing_store is not None:
				Save()

	def Clear(self):
		"""Clear Cache"""

		self.lookup.clear()
		self.items.clear()

		if self.backing_store is not None and os.path.exists(self.backing_store):
			os.remove(self.backing_store)

	def Expire(self):
		"""Expire Elligible Items In Cache"""

		elligible = list()

		for item in self.items:
			if item.expires > datetime.now():
				continue
			else:
				elligible.append(entry.key)

		for item in elligible:
			self.Remove(item,writethrough=False)

		if self.write_through and self.backing_store is not None:
			self.Save()

#
# Support Functions
#

def EnableCache(cachefilename,writethrough,ttl):
	"""Enable Lookup Cache"""

	global LookupCache

	LookupCache = Cache(cachefilename,writethrough,ttl)

# Get Network Block Specifics
def BreakdownNetwork(start,end):
	"""
	Take an IP starting address for a subnet and it's ending address and get the specifics
	for the subnet, including the netmask, number of bits and the CIDR string
	"""

	network = None
	bits = 0
	cidr = None
	count = 0

	if type(start) is str:
		start = ipaddress.ip_address(start)

	if type(end) is str:
		end = ipaddress.ip_address(end)

	summary = ipaddress.summarize_address_range(start,end)

	try:
		net = next(summary)

		network = net.network_address
		netmask = net.netmask
		bits = net.prefixlen
		cidr = net.with_prefixlen
		count = net.num_addresses
	except StopIteration:
		pass
	except Exception as err:
		DbgMsg(err)

	return network,netmask,bits,cidr,count

# Extract Mail Groups From String (user@domain)
def ExtractMailGroups(data):
	"""
	Wrapper function to simplify removing username and domain from poorly deliniated string.
	"""
	m = re.search(loose_emailaddr_exp,data)

	return "{}@{}".format(m.group("username"),m.group("domain"))

# Be more selective about Abuse addresses
def SelectAbuse(items):
	"""
	Wrapper function to selected the best effort email address from a list of email addresses for
	the abuse email. The algorithm is simple, first, try to find "abuse@domain", next, and email
	addres with "abuse" in the user id. All others are added to the potentials list.
	"""
	hit = None

	potentials = []

	for item in items:
		user,domain = item.split("@")

		if re.search("^abuse$",user):
			hit = item
		else:
			potentials.append(item)

	return hit, potentials

# Hunt for email addresses in a List (of possible JSON, Lists or values)
def HuntEmailAddressesInList(items,level=0):
	"""
	Hunt through a JSON document (in this case list in the JSON Doc) for anything resembling an email address
	"""

	addresses = []

	for item in items:
		if type(item) is list:
			addresses.extend(HuntEmailAddressesInList(item,level+1))
		elif type(item) is dict:
			addresses.extend(HuntEmailAddressesInJSON(item,level+1))
		else:
			if type(item) is str and mailcheck(item):
				item = ExtractMailGroups(item)
				addresses.append(item)

	return addresses

# Hunt for email addresses
def HuntEmailAddressesInJSON(jdoc,level=0):
	"""
	Hunt through a JSON document for anything resembling an email address.
	"""

	keys = jdoc.keys()
	addresses = []

	for key in keys:
		value = jdoc[key]

		if type(value) is list:
			addresses.extend(HuntEmailAddressesInList(value,level+1))
		elif type(value) is dict:
			addresses.extend(HuntEmailAddressesInJSON(value,level+1))
		else:
			if type(value) is str and mailcheck(value):
				value = ExtractMailGroups(value)
				addresses.append(value)

	return addresses

# Get Abuse Address
def GetAbuseAddress(jdoc):
	"""
	Wrapper function to hunt through the JSON returned by WHOIS for an abuse email address.

	Failing to find a match, attempt to find any email address with "abuse" in the username
	and failing that, random select any email addres found as the abuse email address.
	"""

	addresses = HuntEmailAddressesInJSON(jdoc)
	potentials = []
	nonpotentials = []

	for address in addresses:
		if type(address) is str and abusecheck(address):
			potentials.append(address)
		else:
			nonpotentials.append(address)

	hit,others = SelectAbuse(potentials)

	if hit is None and (others is None or len(others) == 0):
		return (None,nonpotentials)

	abusemail = hit if hit else random.choice(others) if len(others) > 0 else ""

	return (abusemail,None)

# Make URL
def MkUrl(resource,querydata):
	"""Wrapper function to make well formed URLs"""

	return "{}{}/{}".format(RDAP_URL,resource,querydata)

#
# Whois Functions
#

# Whois Query with Direct RDAP URL
def whois_rdap(url):
	"""Whois RDAP function"""

	DbgMsg("Entering whois_rdap")

	payload = None

	DbgMsg("Executing post...",prefix="XXX")
	response = requests.post(url=url)
	DbgMsg("Post returned",prefix="XXX")

	if response and response.status_code == requests.codes.ok:
		DbgMsg("Post completed successfully",prefix="VVV")
		payload = response.json()
	else:
		DbgMsg(f"Post completed with an error {requests.status_code}",prefix="###")

	return response, payload

# Get IP Info
def GetIPInfo(ipaddr,retry_in=10,pause=0):
	"""Use WHOIS API to get whois info for the supplied IP Address"""
	global ip, LookupCache

	DbgMsg("Entering GetIPInfo")

	retry_count = 0
	retry_limit = 2

	# Init these
	response = payload = None

	# Format :
	# RDAP-Exit-Code, Rec-Name, Rec-Handle, StartAddr, EndAddr, CIDR, parentHandle, abuse, payload, country
	result = WhoisResult(404, None, None, None, None, None, None, None, None, None)

	if IsNetwork(ipaddr):
		ipaddr = ipaddr.rsplit("/")[0]

	if not ValidIP(ipaddr):
		return result

	if LookupCache is not None:
		entry = LookupCache.Exists(ipaddr)

		if entry is not None:
			fields = entry.value.split("|")
			result = WhoisResult(200,fields[0],fields[1],fields[2],fields[3],fields[4],fields[5],fields[6],dict(),fields[8])

			return result

	while retry_count < retry_limit:
		response = payload = None

		try:
			response, payload = whois_rdap(MkUrl(ip,ipaddr))
		except requests.ConnectionError:
			time.sleep(retry_in)			# Most likely a rate limit hit
			retry_count += 1
			continue
		except Exception as err:
			break					# Major bummer

		if response.status_code == 429 and retry_count < retry_limit:
			# Rate Limit
			retry_rate = "Retry-After"

			retry_count += 1

			if retry_rate in response.headers:
				try:
					retry_when = int(response.headers[retry_rate])

					time.sleep(retry_when)
				except:
					time.sleep(retry_in)

		elif response.status_code == 200:
			break					# Gooooood
		else:						# Failsafe
			break

	if payload:
		name = payload.get("name","unknown")
		handle = payload.get("handle","")
		startAddress = payload.get("startAddress",ipaddr)
		endAddress = payload.get("endAddress",ipaddr)
		country = payload.get("country","")

		parentHandle = payload.get("parentHandle","")

		abuse,others = GetAbuseAddress(payload)

		if not abuse:
			abuse = random.choice(others) if len(others) > 0 else ""

		network,netmask,bits,cidr,count = BreakdownNetwork(startAddress,endAddress)

		result = WhoisResult(response.status_code,name,handle,startAddress,endAddress,cidr,parentHandle,abuse,payload,country)
		# result = [ response.status_code, name, handle, startAddress, endAddress, cidr, parentHandle, abuse, payload, country ]

		if LookupCache is not None and response.status_code == 200:
			value = f"{name}|{handle}|{startAddress}|{endAddress}|{cidr}|{parentHandle}|{abuse}||{country}"
			LookupCache.Add(ipaddr,value)
			LookupCache.Expire()

	if pause > 0:
		time.sleep(pause)

	return result

#
# Init and Run Pattern Handler
#

# Build Parser
def BuildParser():
	"""Build Parser"""

	global __Parser__

	if __Parser__ == None:
		parser = __Parser__ = argparse.ArgumentParser(description='Whois Python Module and Utility')

		parser.add_argument("-d","--debug",action="store_true",help="Enter debug mode")
		parser.add_argument("--noshow",action="store_true",help="Return output, but don't display it")
		parser.add_argument("-t",action="store_true",help="Run test function")
		parser.add_argument("-j",action="store_true",help="Return JSON Response")
		parser.add_argument("-s",action="store_true",help="Show header for output")
		parser.add_argument("-p",default=0,help="Add pause in seconds between RDAP calls",required=False)
		parser.add_argument("-f","--file","--whodey",help="File with list of IP's to lookup",required=False)
		parser.add_argument("-c","--cache",help="Lookup Cache file",required=False)
		parser.add_argument("-e","--expires",help="Time in seconds for cache expiration",required=False)
		parser.add_argument("ip",nargs='*',help="IPs to lookup")

# Init Module
def Initialize():
	"""Init Module"""

	BuildParser()

# Init Module
Initialize()

# Run/Plugin/CmdLine Pattern Handler
def run(arguments=None):
	"""Run Pattern Handler"""

	global __Parser__, header

	args = None

	if arguments != None:
		args = __Parser__.parse_args(arguments)
	else:
		args = __Parser__.parse_args()

	info = None

	if args.debug:
		DebugMode(True)
		DbgMsg("Setting to debug mode")

	if args.cache is not None:
		expires = 3600

		if args.expires is not None:
			expires = int(args.expires)

		EnableCache(args.cache,True,expires)

	if args.p != None:
		PauseTime = int(args.p)

	if args.t:
		DbgMsg("Calling test stub")
		test(args)
	elif args.ip != None and args.ip != []:
		DbgMsg("Getting IP Info")

		for ip in args.ip:
			info = GetIPInfo(ip,pause=PauseTime)

			DbgMsg("Checking response\n{}".format(info))
			if info[0] == 200:
				DbgMsg("Attempting to output")

				if args.j and not args.noshow:
					Msg(json.dumps(info[8],indent=2))
				elif not args.noshow:
					if args.s:
						Msg(",".join(header[1:-1]))

					Msg(",".join(info[1:-2]))
			elif not args.noshow:
				Msg("Bummer, RDAP Failed - {}".format(info[0]))
	elif args.file != None:
		DbgMsg("Getting IP Info from file with list of IPs")

		PauseTime = 1		# Set Pause time to a bare minimum

		ips = list()

		with open(args.file,"rt") as fin:
			DbgMsg(f"Reading from {args.file}")

			for ip in fin:
				ips.append(ip.strip())

		DbgMsg("Processed file, getting info")
		for ip in ips:
			info = GetIPInfo(ip,pause=PauseTime)

			if info[0] == 200:
				if args.j and not args.noshow:
					Msg(json.dumps(info[8],indent=2))
				elif not args.noshow:
					if args.s:
						Msg(",".join(header[1:-1]))

					Msg(",".join(info[1:-2]))
	elif not args.noshow:
		Msg("No ip supplied to look up... fool")

	return info

#
# Test Stub
#

# Test Function
def test(args):
	"""Test stub"""

	DebugMode(True)
	ModuleMode(False)

	Msg("I do nothing ATM")
	pass

#
# Main Loop
#

if __name__ == "__main__":
	"""Cmdline Loop"""
	ModuleMode(False)

	run()
