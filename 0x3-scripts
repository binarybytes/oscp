#!/bin/bash

for ip in `seq 1 in 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done


#~$ ./ipsweep.sh 10.92.190 > sweep.txt
#~$ cat sweep.txt 
#threading for faster results
