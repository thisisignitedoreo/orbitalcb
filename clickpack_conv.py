#!/bin/env python

import random
import sys
import zipfile
import shutil
import os
import io

def if_copy(fp1, fp2, top, path, output_path, p):
	if os.path.isdir(os.path.join(path, fp1)) and os.path.isdir(os.path.join(path, fp2)):
		os.mkdir(os.path.join(output_path, p, top))
		os.mkdir(os.path.join(output_path, p, top, "holds"))
		os.mkdir(os.path.join(output_path, p, top, "releases"))
		for i in os.listdir(os.path.join(path, fp1)):
			shutil.copy(os.path.join(path, fp1, i), os.path.join(output_path, p, top, "holds"))
		for i in os.listdir(os.path.join(path, fp2)):
			shutil.copy(os.path.join(path, fp2, i), os.path.join(output_path, p, top, "releases"))

def zcb_live(path, output_path, name, options=set(), p="p1"):
	os.mkdir(os.path.join(output_path, p))
	os.mkdir(os.path.join(output_path, p, "holds"))
	os.mkdir(os.path.join(output_path, p, "releases"))
	
	for i in os.listdir(os.path.join(path, "clicks")):
		shutil.copy(os.path.join(path, "clicks", i), os.path.join(output_path, p, "holds"))
	for i in os.listdir(os.path.join(path, "releases")):
		shutil.copy(os.path.join(path, "releases", i), os.path.join(output_path, p, "releases"))

	if_copy("softClicks", "softReleases", "softclicks", path, output_path, p)
	if_copy("softclicks", "softreleases", "softclicks", path, output_path, p)
	if_copy("soft clicks", "soft releases", "softclicks", path, output_path, p)
	if_copy("soft-clicks", "soft-releases", "softclicks", path, output_path, p)
	if_copy("soft Clicks", "soft Releases", "softclicks", path, output_path, p)
	if_copy("soft-Clicks", "soft-Releases", "softclicks", path, output_path, p)

	if_copy("hardClicks", "hardReleases", "hardclicks", path, output_path, p)
	if_copy("hardclicks", "hardreleases", "hardclicks", path, output_path, p)
	if_copy("hard clicks", "hard releases", "hardclicks", path, output_path, p)
	if_copy("hard-clicks", "hard-releases", "hardclicks", path, output_path, p)
	if_copy("hard Clicks", "hard Releases", "hardclicks", path, output_path, p)
	if_copy("hard-Clicks", "hard-Releases", "hardclicks", path, output_path, p)
	
	if any(map(lambda x: x.startswith(("bgn", "whitenoise")), os.listdir(path))):
		for i in filter(lambda x: x.startswith("bgn"), os.listdir(path)):
			fmt = i.rsplit(".", 1)[1]
			shutil.copy(os.path.join(path, i), os.path.join(output_path, f'bg-noise.{fmt}'))

	open(os.path.join(output_path, "meta.json"), "w").write('{' + f'"name": "{repr(name)[1:-1]}", "description": "auto-translated from zcb-live clickpack", "author": "???"' + '}')

	if "p2" in options: zcb_live(path, output_path, set(), "p2")

def from_memory(blob, fn, name=""):
	folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))
	while os.path.isdir(os.path.join(temp_folder, folder)):
		folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))

	os.mkdir(os.path.join(temp_folder, folder))

	with zipfile.ZipFile(io.BytesIO(blob)) as f:
		f.extractall(os.path.join(temp_folder, folder))
		
	inp = os.path.join(temp_folder, folder)

	folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))
	while os.path.isdir(os.path.join(temp_folder, folder)):
		folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))

	os.mkdir(os.path.join(temp_folder, folder))
	
	output_folder = os.path.join(temp_folder, folder)

	fn(inp, output_folder, name, set("p2" if "--p2" in sys.argv else ""))

	return output_folder

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

