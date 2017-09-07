#!/bin/python

import sys
print "Enter the number"
a = int(raw_input())
temp = a
reverse = 0

while a>0:
	reminder = a%10
	reverse = reverse * 10 + reminder
	a = a/10

if temp == reverse:
	print "Palindrome"
else:
	print "Not Palindrome"