#!/bin/env python

import random
import sys
import zipfile
import shutil
import os

def zcb_live(path, output_path, name, options=set(), p="p1"):
	os.mkdir(os.path.join(output_path, p))
	os.mkdir(os.path.join(output_path, p, "holds"))
	os.mkdir(os.path.join(output_path, p, "releases"))
	
	for i in os.listdir(os.path.join(path, "clicks")):
		shutil.copy(os.path.join(path, "clicks", i), os.path.join(output_path, p, "holds"))
	for i in os.listdir(os.path.join(path, "releases")):
		shutil.copy(os.path.join(path, "releases", i), os.path.join(output_path, p, "releases"))

	if os.path.isdir(os.path.join(path, "softClicks")) and os.path.isdir(os.path.join(path, "softReleases")):
		os.mkdir(os.path.join(output_path, p, "softclicks"))
		os.mkdir(os.path.join(output_path, p, "softclicks", "holds"))
		os.mkdir(os.path.join(output_path, p, "softclicks", "releases"))
		for i in os.listdir(os.path.join(path, "softClicks")):
			shutil.copy(os.path.join(path, "softClicks", i), os.path.join(output_path, p, "softclicks", "holds"))
		for i in os.listdir(os.path.join(path, "softReleases")):
			shutil.copy(os.path.join(path, "softReleases", i), os.path.join(output_path, p, "softclicks", "releases"))

	if os.path.isdir(os.path.join(path, "hardClicks")) and os.path.isdir(os.path.join(path, "hardReleases")):
		os.mkdir(os.path.join(output_path, p, "hardclicks"))
		os.mkdir(os.path.join(output_path, p, "hardclicks", "holds"))
		os.mkdir(os.path.join(output_path, p, "hardclicks", "releases"))
		for i in os.listdir(os.path.join(path, "hardClicks")):
			shutil.copy(os.path.join(path, "hardClicks", i), os.path.join(output_path, p, "hardclicks", "holds"))
		for i in os.listdir(os.path.join(path, "hardReleases")):
			shutil.copy(os.path.join(path, "hardReleases", i), os.path.join(output_path, p, "hardclicks", "releases"))
	
	if any(map(lambda x: x.startswith("bgn"), os.listdir(path))):
		for i in filter(lambda x: x.startswith("bgn"), os.listdir(path)):
			fmt = i.rsplit(".", 1)[1]
			shutil.copy(os.path.join(path, i), os.path.join(output_path, f'bg-noise.{fmt}'))

	open(os.path.join(output_path, "meta.json"), "w").write('{' + f'"name": "{repr(name)[1:-1]}", "description": "auto-translated from zcb-live clickpack", "author": "???"' + '}')

	if "p2" in options: zcb_live(path, output_path, set(), "p2")

usage = f'usage: {sys.argv[0]} <original format> <clickpack archive/folder> <output file>'
temp_folder = "/tmp/" if os.name == "posix" else os.getenv("temp")

if __name__ == "__main__":
	if len(sys.argv) < 4:
		print(usage)
		exit()

	formats = {
		"zcb-live": zcb_live
	}

	fmt, inp, outp = sys.argv[1:4]
	
	if fmt not in formats:
		print(usage)
		print(f'formats: {", ".join(formats.keys())}')
		exit()

	name = os.path.basename(inp).rsplit(".", 1)[0]

	if os.path.isfile(inp):
		if not zipfile.is_zipfile(inp): exit()
		
		folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))
		while os.path.isdir(os.path.join(temp_folder, folder)):
			folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))

		os.mkdir(os.path.join(temp_folder, folder))

		with zipfile.ZipFile(inp) as f:
			f.extractall(os.path.join(temp_folder, folder))
		
		inp = os.path.join(temp_folder, folder)

	folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))
	while os.path.isdir(os.path.join(temp_folder, folder)):
		folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))

	os.mkdir(os.path.join(temp_folder, folder))
	
	output_folder = os.path.join(temp_folder, folder)

	formats[fmt](inp, output_folder, name, set("p2" if "--p2" in sys.argv else ""))

	shutil.make_archive(outp[:-4], "zip", output_folder)

