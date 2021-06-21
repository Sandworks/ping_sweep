#!/usr/bin/env python3

# Filename: ping_sweep.py
# Author:   James Sanders
# Version:  1.1

# Import dependencies
import json
import sys
from pythonping import ping

# check we received correct argument.
if len(sys.argv) == 2:
	jsonfile = sys.argv[1]
	
elif len(sys.argv) == 1:
	sys.exit("Usage: {} <json file>".format(sys.argv[0]))	

elif len(sys.argv) > 2:
	print ("Too many arguments")
	sys.exit()

# gather device details from a JSON file
with open(jsonfile) as file:
    devices = json.load(file)

    # check responsive for each device
    for device in devices["devices"]:
        search_string = "Reply from " + device["ip"]
        # if output contains "Reply from <ip>" then is successful.
        if search_string in str(ping(device["ip"])):
            # if successful
            print("   hostname: {} ({}) is up".format(device["name"], device["ip"]))
        else:
            # if failed
            print("** hostname: {} ({}) is down".format(device["name"], device["ip"]))

# task complete    
print ('Ping task complete')
