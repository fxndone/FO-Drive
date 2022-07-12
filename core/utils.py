from . import *

import requests
import sys
import re

TEMP_DIRS = []

def extract_filename(headers):
    content = headers.get('content-disposition')
    if content is None:
        return False
    filename = re.findall("filename=(.+)", content)
    if len(filename) == 0:
        return False
    return filename[0]

def full_exit():
    print("\n[+] Exiting...")
    sys.exit(0)

def cleared(string):
    output = string
    for e in (' ', '\n', '\t', '\r'):
        output = output.replace(e, '')
    return output