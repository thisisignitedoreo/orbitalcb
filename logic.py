
from pydub import AudioSegment
import fnmatch
import zipfile
import random
import struct
import json
import os

def read_f32(f):
    return struct.unpack('f', f.read(4))[0]

def read_u32(f):
    return struct.unpack('I', f.read(4))[0]

def parse_re_replay(length, fd):
    replay = []
    for i in range(length):
        st = struct.unpack('I?i?xxx', fd.read(16))
        replay.append({"frame": st[0], "hold": st[1], "player": 1 if st[3] else 2})
    return replay

def parse_re_macro(path):
    macro = {}
    with open(path, "rb") as f:
        macro["tps"] = read_f32(f)
        phys_replay_length = read_u32(f)
        frame_replay_length = read_u32(f)
        f.read(phys_replay_length * struct.calcsize('Ifffd?xxxxxxx'))
        macro["replay"] = parse_re_replay(frame_replay_length, f)
    return macro

macro_types = {
    ("ReplayEngine", "*.re"): parse_re_macro,
}


# god forgive me i wrote it on 02:40

class Clickpack:
    def __init__(self, path):
        self.data = {
            "p1": {
                "holds": [],
                "releases": [],
                "softclicks": {
                    "holds": [],
                    "releases": [],
                },
                "hardclicks": {
                    "holds": [],
                    "releases": [],
                },
            },
            "p2": {
                "holds": [],
                "releases": [],
                "softclicks": {
                    "holds": [],
                    "releases": [],
                },
                "hardclicks": {
                    "holds": [],
                    "releases": [],
                },
            },
        }
        
        sc = True
        hc = True
        p2 = True
        p2sc = True
        p2hc = True

        # SOFT&HARD CLICKS

        required = [
            os.path.join(path, "p1", "softclicks"),
            os.path.join(path, "p1", "softclicks", "holds"),
            os.path.join(path, "p1", "softclicks", "releases"),
        ]

        for i in required: sc = sc and os.path.isdir(i)

        required = [
            os.path.join(path, "p1", "hardclicks"),
            os.path.join(path, "p1", "hardclicks", "holds"),
            os.path.join(path, "p1", "hardclicks", "releases"),
        ]

        for i in required: hc = hc and os.path.isdir(i)
        
        if sc:
            required = [
                os.path.join(path, "p1", "softclicks", "holds"),
                os.path.join(path, "p1", "softclicks", "releases"),
            ]

            for i in required: sc = sc and any([j.endswith(("ogg", "mp3", "wav", "flac")) for j in os.listdir(i)])
        
        if hc:
            required = [
                os.path.join(path, "p1", "hardclicks", "holds"),
                os.path.join(path, "p1", "hardclicks", "releases"),
            ]

            for i in required: hc = hc and any([j.endswith(("ogg", "mp3", "wav", "flac")) for j in os.listdir(i)])

        # PLAYER 2
        required = [
            os.path.join(path, "p2"),
            os.path.join(path, "p2", "holds"),
            os.path.join(path, "p2", "releases"),
        ]

        for i in required: p2 = p2 and os.path.isdir(i)

        if p2:
            required = [
                os.path.join(path, "p2", "holds"),
                os.path.join(path, "p2", "releases"),
            ]

            for i in required: p2 = p2 and any([j.endswith(("ogg", "mp3", "flac", "wav")) for j in os.listdir(i)])

        if p2:
            required = [
                os.path.join(path, "p2", "softclicks"),
                os.path.join(path, "p2", "softclicks", "holds"),
                os.path.join(path, "p2", "softclicks", "releases"),
            ]

            for i in required: p2sc = p2sc and os.path.isdir(i)

            required = [
                os.path.join(path, "p2", "hardclicks"),
                os.path.join(path, "p2", "hardclicks", "holds"),
                os.path.join(path, "p2", "hardclicks", "releases"),
            ]

            for i in required: p2hc = p2hc and os.path.isdir(i)
        
            if p2sc:
                required = [
                    os.path.join(path, "p2", "softclicks", "holds"),
                    os.path.join(path, "p2", "softclicks", "releases"),
                ]

                for i in required: p2sc = p2sc and any([j.endswith(("ogg", "mp3", "wav", "flac")) for j in os.listdir(i)])
        
            if p2hc:
                required = [
                    os.path.join(path, "p2", "hardclicks", "holds"),
                    os.path.join(path, "p2", "hardclicks", "releases"),
                ]

                for i in required: p2hc = p2hc and any([j.endswith(("ogg", "mp3", "wav", "flac")) for j in os.listdir(i)])

        # filling up self.data

        for i in os.listdir(os.path.join(path, "p1", "holds")):
            if i.endswith(("ogg", "wav", "mp3", "flac")):
                self.data["p1"]["holds"].append(AudioSegment.from_file(os.path.join(path, "p1", "holds", i,), i.rsplit(".", 1)[-1]))

        for i in os.listdir(os.path.join(path, "p1", "releases")):
            if i.endswith(("ogg", "wav", "mp3", "flac")):
                self.data["p1"]["releases"].append(AudioSegment.from_file(os.path.join(path, "p1", "releases", i,), i.rsplit(".", 1)[-1]))
        
        if sc:
            for i in os.listdir(os.path.join(path, "p1", "softclicks", "holds")):
                if i.endswith(("ogg", "wav", "mp3", "flac")):
                    self.data["p1"]["softclicks"]["holds"].append(AudioSegment.from_file(os.path.join(path, "p1", "softclicks", "holds", i,), i.rsplit(".", 1)[-1]))

            for i in os.listdir(os.path.join(path, "p1", "softclicks", "releases")):
                if i.endswith(("ogg", "wav", "mp3", "flac")):
                    self.data["p1"]["softclicks"]["releases"].append(AudioSegment.from_file(os.path.join(path, "p1", "softclicks", "releases", i,), i.rsplit(".", 1)[-1]))

        if hc:
            for i in os.listdir(os.path.join(path, "p1", "hardclicks", "holds")):
                if i.endswith(("ogg", "wav", "mp3", "flac")):
                    self.data["p1"]["hardclicks"]["holds"].append(AudioSegment.from_file(os.path.join(path, "p1", "hardclicks", "holds", i,), i.rsplit(".", 1)[-1]))

            for i in os.listdir(os.path.join(path, "p1", "hardclicks", "releases")):
                if i.endswith(("ogg", "wav", "mp3", "flac")):
                    self.data["p1"]["hardclicks"]["releases"].append(AudioSegment.from_file(os.path.join(path, "p1", "hardclicks", "releases", i,), i.rsplit(".", 1)[-1]))

        if p2:
            for i in os.listdir(os.path.join(path, "p2", "holds")):
                if i.endswith(("ogg", "wav", "mp3", "flac")):
                    self.data["p2"]["holds"].append(AudioSegment.from_file(os.path.join(path, "p2", "holds", i,), i.rsplit(".", 1)[-1]))

            for i in os.listdir(os.path.join(path, "p2", "releases")):
                if i.endswith(("ogg", "wav", "mp3", "flac")):
                    self.data["p2"]["releases"].append(AudioSegment.from_file(os.path.join(path, "p2", "releases", i,), i.rsplit(".", 1)[-1]))
            
            if p2sc:
                for i in os.listdir(os.path.join(path, "p2", "softclicks", "holds")):
                    if i.endswith(("ogg", "wav", "mp3", "flac")):
                        self.data["p2"]["softclicks"]["holds"].append(AudioSegment.from_file(os.path.join(path, "p2", "softclicks", "holds", i,), i.rsplit(".", 1)[-1]))

                for i in os.listdir(os.path.join(path, "p2", "softclicks", "releases")):
                    if i.endswith(("ogg", "wav", "mp3", "flac")):
                        self.data["p2"]["softclicks"]["releases"].append(AudioSegment.from_file(os.path.join(path, "p2", "softclicks", "releases", i,), i.rsplit(".", 1)[-1]))

            if p2hc:
                for i in os.listdir(os.path.join(path, "p2", "hardclicks", "holds")):
                    if i.endswith(("ogg", "wav", "mp3", "flac")):
                        self.data["p2"]["hardclicks"]["holds"].append(AudioSegment.from_file(os.path.join(path, "p2", "hardclicks", "holds", i,), i.rsplit(".", 1)[-1]))

                for i in os.listdir(os.path.join(path, "p2", "hardclicks", "releases")):
                    if i.endswith(("ogg", "wav", "mp3", "flac")):
                        self.data["p2"]["hardclicks"]["releases"].append(AudioSegment.from_file(os.path.join(path, "p2", "hardclicks", "releases", i,), i.rsplit(".", 1)[-1]))
        
        if not sc: self.data["p1"]["softclicks"] = None
        if not hc: self.data["p1"]["hardclicks"] = None
        if not p2: self.data["p2"] = self.data["p1"]
        else:
            if not p2sc: self.data["p2"]["softclicks"] = None
            if not p2hc: self.data["p2"]["hardclicks"] = None


def render(macro_path, clickpack_path, output_path, options):
    if zipfile.is_zipfile(clickpack_path):
        temp_folder = "/tmp/" if os.name == "posix" else os.getenv("temp")

        folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))
        while os.path.isdir(os.path.join(temp_folder, folder)):
            folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))

        os.mkdir(os.path.join(temp_folder, folder))

        with zipfile.ZipFile(clickpack_path) as f:
            f.extractall(os.path.join(temp_folder, folder))
        return render(macro_path, os.path.join(temp_folder, folder), output_path, options)

    for k, i in macro_types.items():
        if fnmatch.fnmatch(macro_path, k[1]):
            macro = i(macro_path)
            break

    last_frame = macro["replay"][-1]["frame"]

    duration = last_frame / macro["tps"] * 1000 + options["end"] * 1000

    output = AudioSegment.silent(duration=duration)

    clickpack = Clickpack(clickpack_path)
    

    p1_click_delta = 0
    p2_click_delta = 0

    p1_last_click = 0
    p2_last_click = 0

    for k, i in enumerate(macro["replay"], start=1):
        options["progress_callback"](k, len(macro["replay"]))

        if i["player"] == 1:
            p1_click_delta = i["frame"] - p1_last_click

            sound = None
            if options["softclicks"] is not None \
                    and clickpack.data["p1"]["softclicks"] is not None \
                    and p1_click_delta <= options["softclicks"]:
                sound = random.choice(clickpack.data["p1"]["softclicks"]["holds" if i["hold"] else "releases"])
            elif options["hardclicks"] is not None \
                    and clickpack.data["p1"]["hardclicks"] is not None \
                    and p1_click_delta >= options["hardclicks"]:
                sound = random.choice(clickpack.data["p1"]["hardclicks"]["holds" if i["hold"] else "releases"])
            else:
                sound = random.choice(clickpack.data["p1"]["holds" if i["hold"] else "releases"])

            p1_last_click = i["frame"]
        
        elif i["player"] == 2:
            p2_click_delta = i["frame"] - p2_last_click

            sound = None
            if options["softclicks"] is not None \
                    and clickpack.data["p2"]["softclicks"] is not None \
                    and p2_click_delta <= options["softclicks"]:
                sound = random.choice(clickpack.data["p2"]["softclicks"]["holds" if i["hold"] else "releases"])
            elif options["hardclicks"] is not None \
                    and clickpack.data["p2"]["hardclicks"] is not None \
                    and p2_click_delta >= options["hardclicks"]:
                sound = random.choice(clickpack.data["p2"]["hardclicks"]["holds" if i["hold"] else "releases"])
            else:
                sound = random.choice(clickpack.data["p2"]["holds" if i["hold"] else "releases"])

            p2_last_click = i["frame"]
        
        position = i["frame"] / macro["tps"] * 1000
        output = output.overlay(sound, position=position)
    
    output.export(output_path, output_path.rsplit(".", 1)[-1])

def clickpack_info(clickpack_path):
    if os.path.isfile(clickpack_path):
        if not zipfile.is_zipfile(clickpack_path): return ("", "", "")

        temp_folder = "/tmp/" if os.name == "posix" else os.getenv("temp")

        folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))
        while os.path.isdir(os.path.join(temp_folder, folder)):
            folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))

        os.mkdir(os.path.join(temp_folder, folder))

        with zipfile.ZipFile(clickpack_path) as f:
            f.extractall(os.path.join(temp_folder, folder))
        
        clickpack_path = os.path.join(temp_folder, folder)

    if not os.path.isfile(os.path.join(clickpack_path, "meta.json")):
        return ("", "", "")
    else:
        json_meta = json.load(open(os.path.join(clickpack_path, "meta.json")))
        if not ("name" in json_meta.keys() and "author" in json_meta.keys() and "description" in json_meta.keys()):
            return ("", "", "")
        return (json_meta["name"], json_meta["author"], json_meta["description"])

def macro_info(macro_path):
    for i, c in macro_types.items():
        if fnmatch.fnmatch(macro_path, i[1]):
            return (c(macro_path)["tps"], )

def is_clickpack(clickpack_path):
    if os.path.isdir(clickpack_path):
        required = [
            os.path.join(clickpack_path, "p1"),
            os.path.join(clickpack_path, "p1", "holds"),
            os.path.join(clickpack_path, "p1", "releases"),
        ]
        
        for i in required:
            if not os.path.isdir(i): return False

        required = [
            os.path.join(clickpack_path, "p1", "holds"),
            os.path.join(clickpack_path, "p1", "releases"),
        ]

        for i in required:
            if len([j.endswith(("wav", "ogg", "flac", "mp3")) for j in os.listdir(i)]) == 0: return False

        return True
    
    elif os.path.isfile(clickpack_path):
        if not zipfile.is_zipfile(clickpack_path): return False

        temp_folder = "/tmp/" if os.name == "posix" else os.getenv("temp")

        folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))
        while os.path.isdir(os.path.join(temp_folder, folder)):
            folder = "_ORBITAL" + str(random.randint(100000000000000000, 999999999999999999))

        os.mkdir(os.path.join(temp_folder, folder))

        with zipfile.ZipFile(clickpack_path) as f:
            f.extractall(os.path.join(temp_folder, folder))

        return is_clickpack(os.path.join(temp_folder, folder))

def is_macro(macro_path):
    return any([fnmatch.fnmatch(macro_path, i[1]) for i in macro_types.keys()])

