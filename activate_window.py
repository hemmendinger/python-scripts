import os
import subprocess

def get_process(name):
    """Search for the windows containing name and return list of IDs"""
    window_ids = subprocess.check_output(["xdotool", "search", "--name", name])
    window_ids = window_ids.splitlines() # split str by linebreaks
    return window_ids

def activate_window(window_id):
    for identifier in window_id:
        subprocess.call(["xdotool", "windowactivate", identifier ])


if __name__ == '__main__':
    print get_process("emacs")

