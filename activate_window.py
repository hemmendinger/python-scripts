"""
Activate the window of a program under Ubuntu/Linux.

Dependency:
    xdotools
    Python (Tested using Python 2.7.3 and Python 3.2.3)

Usage:
    python activate_window.py NAME_OF_PROGRAM

Purpose:
Alt-Tab can be an unnecessary strain on the wrists during extended
coding sessions.

If you find yourself needing to use Alt-Tab with a bunch of windows
open, and you usually just want to switch back to a text editor or
browser, assign this script to a shortcut.
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
