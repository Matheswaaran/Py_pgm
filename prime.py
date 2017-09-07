#!/bin/python
import sys

def isPrime(n):
	count = 0
	for i in range(1,n):
		if n%1 == 0:
			count = count + 1

	if count == 2:
		return True
	else:
		return False

n = int(raw_input())
if isPrime(n) == True:
	print "Prime"
else:
	print "Not Prime"
