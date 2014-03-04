import os
import subprocess

def get_process(process):
    pid = subprocess.check_output(["pgrep", process])
    pid = pid.strip() # remove trailing linebreak


def test(process):
    pid = call(["pgrep", process])
    print pid

if __name__ == '__main__':
    get_process("emacs")

