


#!/bin/bash


for ip in $(cat iplist.txt); do nmap -p 80 -T4 $ip & done


#threading ips and scanning against nmap to check whats open on port 80
