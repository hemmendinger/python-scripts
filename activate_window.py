"""
Activate the window of a program.

Usage:
    python activate_window.py NAME_OF_PROGRAM

"""

from sys import argv
import subprocess


def get_process(name):
    """Search for visible windows containing name, returns list of IDs"""
    window_ids = subprocess.check_output(["xdotool", "search", "--onlyvisible", "--name", name])
    window_ids = window_ids.splitlines() # split str by linebreaks
    return window_ids

def activate_window(window_ids):
    """Iterates the identifiers, trying to activate each one"""
    for identifier in window_ids:
        subprocess.call(["xdotool", "windowactivate", identifier])


if __name__ == '__main__':
    process = get_process(argv[1])
    activate_window(process)
