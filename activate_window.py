import os
import subprocess

def get_process(name):
    """Search for the windows containing name and return list of IDs"""
    window_ids = subprocess.check_output(["xdotool", "search", "--onlyvisible", "--name", name])
    window_ids = window_ids.splitlines() # split str by linebreaks
    return window_ids

def activate_window(window_ids):
    """Iterates the identifiers, trying to activate each one"""
    for identifier in window_ids:
        subprocess.call(["xdotool", "windowactivate", identifier])


if __name__ == '__main__':
     get_process("emacs")

