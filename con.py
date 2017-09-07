#!/bin/python

f=open('players.csv','r')

dic1 = {}
headers = []



for line in f.readlines():
	line = line.rstrip('\n')
	players = []
	d1 = {}
	words = line.split(',')
	print(words)
f.close()