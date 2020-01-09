#!/usr/bin/python

import datetime from datetime
from multiprocessing.pool import ThreadPool
import os

RES_ARR=[]
  
print("-"*50)
print("start time: "+str(datetime.now()))
print("-"*50)

#add color somewhere doodz
print("welcome...)

def ping(host):
  results = os.system("ping -c 1 -W1 %s > /dev/null", % host)
      if results == 0:
        RES_ARR.append("%s" % host)
       else:
        NMAP_ARR.append(host)
