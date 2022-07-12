from . import *

import shutil
import os


def make_zip(output_name, dir_path):
    try:
        output = os.path.join(generate_temp_dir(), output_name)
        shutil.make_archive(output, 'zip', dir_path)
        return output + ".zip"
    except:
        return False


def extract_zip(filename, dir_path):
    try:
        shutil.unpack_archive(filename, dir_path)
        return dir_path
    except:
        return False