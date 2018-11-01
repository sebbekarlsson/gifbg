from gifbg import DIRECTORY
import glob
import os


def get_files():
    return sorted(
        glob.glob(os.path.join(DIRECTORY, '*.png')),
        key=lambda x: int(x.split('-')[1].split('.')[0])
    )
