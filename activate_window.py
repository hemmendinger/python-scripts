import os
import subprocess

def get_process(process):
    pid = subprocess.check_output(["xdotool", "search", "--name", process])
    pid = pid.splitlines() # split str by linebreaks


def test(process):
    pid = call(["pgrep", process])
    print pid

if __name__ == '__main__':
    get_process("emacs")

