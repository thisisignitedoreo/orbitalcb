#!/bin/env python

import logic as cb
import sys
import os

stfu = False

def log(*args, end="\n", sep=" "):
	if not stfu:
		print(*args, end=end, sep=sep)

def error(string):
	print(string)
	exit(1)

def print_usage(prg):
	print(f"usage: {prg} <macro> <clickpack> <output> [--stfu]")

def parse_args(args):
	program = args.pop(0)
	if len(args) == 0:
		print_usage(program)
		exit(1)
	
	macro, clickpack, output = None, None, None
	p = 0
	stfu = False
	for i in args:
		if i == "--stfu":
			stfu = True
		else:
			if p == 0: macro = i
			elif p == 1: clickpack = i
			elif p == 2: output = i
			else:
				print_usage(program)
				error("too many positional args")
			p += 1
	if any(map(lambda x: x is None, [macro, clickpack, output])):
		print_usage(program)
		error("not enough positional args")
	return macro, clickpack, output, stfu

def progress(v, x):
	log(f"{v/x*100:.2f}%", end="\r")

if __name__ == "__main__":
	macro, clickpack, output, stfu = parse_args(sys.argv)

	if not (os.path.isfile(macro) and cb.is_macro(macro)): error("no such file or not a macro")
	if not (os.path.isfile(clickpack) and cb.is_clickpack(clickpack)): error("no such file/folder or not a click path")
	
	sc, hc, end = 200, 500, 3

	clickp_info = cb.clickpack_info(clickpack)
	log("macro info:")
	log(f" tps: {cb.macro_info(macro)[0]}")
	log("clickpack info:")
	log(f" name: {clickp_info[0] if clickp_info[0] else 'unspecified'}")
	log(f" description:{' unspecified' if not clickp_info[2] else ''}")
	if clickp_info[1]:
		for i in clickp_info[2].split('\n'):
			log(f'  {i}')
	log(f" author: {clickp_info[1] if clickp_info[1] else 'unspecified'}")

	cb.render(macro, clickpack, output, {"softclicks": sc, "hardclicks": hc, "end": end, "progress_callback": progress})
	log()

