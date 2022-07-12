from . import *

import os

if not os.path.isfile("config.cfg"):
    print("[!] File \"config.cfg\" not found !")
    print("[!] This file is required !")
    print("[!] See README.md to see how to configure")
    full_exit()

URL = DIR = USER = None

with open("config.cfg", 'r') as f:
    for line in f.read().split('\n'):
        if not line:
            continue
        if cleared(line).startswith('URL='):
            URL = cleared(line.split('=')[1])
        elif cleared(line).startswith('DIRECTORY='):
            DIR = line.split('=')[1]
            while DIR.startswith(' '):
                DIR = DIR[1:]
        elif cleared(line).startswith('USER='):
            USER = cleared(line.split('=')[1])
        elif cleared(line).startswith('PASSWORD=') or cleared(line).startswith('PASS='):
            print("[!] Please do not put your password on clear on the config file !")
            print("[!] Anyone who could read \"config.cfg\" could read your password !")
            print("[!] See README.md please")
            full_exit()

if URL is None or DIR is None or USER is None:
    print("[!] Bad \"config.cfg\" file found !")
    print("[!] Please see README.md to see how to configure")
    full_exit()