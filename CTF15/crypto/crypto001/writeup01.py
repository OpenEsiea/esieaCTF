#!/usr/bin/python

import os
import time

message = "cqgcy{yjjwmspzyqcypczcjmlermsq}"
nbtime = 0
mymsg = ""

def decrypt(n):
	newc = 0
	todd = 0
	decrypted = ""
	for i in range(0,len(message)):
		if message[i] != '{' and message[i] != '}':
			if ord(message[i]) + n > 122:
				toadd = (ord(message[i]) + n) - 122
				newc = 96 + toadd
			else:	
				newc = ord(message[i]) + n
			decrypted = decrypted + chr(newc)
			i= i + 1

	return decrypted

while(1):
	for i in range(1, 10):
		print decrypt(i)
		if i == 9:
			exit(1)
		i = i + 1
	time.sleep(2)
