#!/usr/bin/python

import sockets


s = sockets.socket(socket.AF_INET, socket.SOCK_STREAM)
data = s.recv(1024)

#test out the loop for getting and printing banners/replyz
def data:
  print(s.recv(1024))
   


print("send bad bufferz")
s.connect(('1.2.3.4', 110))  #connect to IP + POP3 port
print(data) #get+print reply

s.send('USER test' + '\r\n') #send uname test
print(data) #get+print reply

s.send('PASS test' + '\r\n' #send pwd test
print(data) #get+print reply

s.close()   #close socket
print("done!" +\n) 
