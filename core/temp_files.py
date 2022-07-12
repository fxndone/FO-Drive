from . import *

import tempfile
import shutil


def generate_temp_dir():
    tmp = tempfile.mkdtemp()
    TEMP_DIRS.append(tmp)
    return tmp

def delet_directory(directory):
    try:
        shutil.rmtree(directory)
        return True
    except:
        return False

def clear_dirs():
    for tmp in TEMP_DIRS:
        delet_directory(tmp)
    TEMP_DIRS.clear()