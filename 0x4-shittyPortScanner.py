#!/bin/python3

#----------#
#  unikz   #
#----------#

#v1 shitty portscanner by unikzzz -- no threading

import sys #cmd arguments++
import socket  #connect to afinet and do soc streaming, port++
from datetime import datetime

#define target

#python3 pscan.py <ip>

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4

else:
	print("invalid amound of argumentz!")
	print("syntax: python3 scanner.py <ip>")
	sys.exit()

#banner++
print("-" * 50)
print("scanning target "+target)
print("time started: "+str(datetime.now()))
print("-" * 50) 

#AF_INET is ipv4
#sockstream is your port

try: 
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #float;moves on after 1 second
		result = s.connect_ex((target,port)) #error indicator
		print("checking port {}...".format(port))
		if result == 0:
			print("Port {} is open".format(port))	
		s.close()


except KeyboardInterrupt:
	print("\nexiting program...")
	sys.exit()

except socket.gaierror:
	print("hostname could not be resolved.")

except socket.error:
	print("couldnt connect to server")
	sys.exit()
