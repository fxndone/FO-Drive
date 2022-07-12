import tempfile
import shutil


def generate_temp_dir():
    return tempfile.mkdtemp()

def delet_directory(directory):
    try:
        shutil.rmtree(directory)
        return True
    except:
        return False