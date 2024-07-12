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
	sys.exit(1)

def print_usage(prg):
	print(f"usage: {prg} <macro> <clickpack> <output> [--stfu] [--no-noise]")

def parse_args(args):
	program = args.pop(0)
	if len(args) == 0:
		print_usage(program)
		sys.exit(1)
	
	macro, clickpack, output = None, None, None
	p = 0
	docmd = True
	noise = True
	stfu = False
	for i in args:
		if docmd and i == "--stfu": stfu = True
		elif docmd and i == "--no-noise": noise = False
		elif docmd and i == "--": docmd = False
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
	return macro, clickpack, output, noise, stfu

def progress(v, x):
	log(f"{v/x*100:.2f}%", end="\r")

if __name__ == "__main__":
	macro, clickpack, output, noise, stfu = parse_args(sys.argv)

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
	has_noise = "yes" if clickp_info[3] else "no"
	log(f" has noise: {has_noise}")

	cb.render(macro, clickpack, output, {"softclicks": sc, "hardclicks": hc, "end": end, "progress_callback": progress, "noise": noise})
	log()

