import os


DIRECTORY = os.path.join(os.path.expanduser("~"), '.gifbg')


if not os.path.isdir(DIRECTORY):
    os.makedirs(DIRECTORY)
