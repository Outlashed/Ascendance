import os
import sys
import subprocess
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
script = SCRIPT_DIR / 'ascendance.py'


def open_terminal():
    if sys.platform.startswith('win'):
        subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', f'python "{script}"'], shell=True)
    elif sys.platform.startswith('darwin'):
        subprocess.Popen(['open', '-a', 'Terminal', str(script)])
    else:
        term = shutil.which('x-terminal-emulator') or shutil.which('gnome-terminal') or shutil.which('xterm')
        if term:
            subprocess.Popen([term, '-e', f'python "{script}"'])
        else:
            print('No terminal emulator found. Running directly.')
            subprocess.call([sys.executable, str(script)])


if __name__ == '__main__':
    open_terminal()
