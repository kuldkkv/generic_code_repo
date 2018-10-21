#!/usr/bin/env python

#import argparse
import string
import random

str_chars = string.ascii_letters + string.digits + '_-=-'
num_chars = string.digits
str1 = 'S:13,S:10,S:30,S:8,S:7,N:6,S:16,N:3,S:7,S:18,N:1,N:3,N:3,N:3,N:5,N:3,S:22,S:27,S:11,S:10,S:27,S:11,S:17,N:2,N:8,N:5,N:3'
num_lines = 10000 * 100

def gen_rand_str(size=30, chars=str_chars):
	return '"' + ''.join(random.choice(chars) for _ in range(size)) + '"'

def gen_rand_num(size=5, chars=num_chars):
	return ''.join(random.choice(chars) for _ in range(size))

func_list = list()
func_args = list()

for fld in str1.split(','):
	(dt, dt_len) = fld.split(':')
	if dt == 'S':
		func_list.append(gen_rand_str)
	else:
		func_list.append(gen_rand_num)
	func_args.append(int(dt_len))

for i in range(num_lines):
	delim = ''
	for j in range(len(func_list)):
		print(delim + func_list[j](func_args[j]), end='')
		delim = ','
	print('')

