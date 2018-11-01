from gifbg.utils import get_files
import subprocess
import time


if __name__ == '__main__':
    try:
        while True:
            for f in get_files():
                subprocess.Popen(['feh', '--bg-fill', f])
                time.sleep(0.2)
    except KeyboardInterrupt:
        quit()
