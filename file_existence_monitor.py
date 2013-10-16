"""
Notify if files in a directory have changed, but only by file names.

Usage:
python script.py FILENAME_TO_WATCH NUMBER_OF_TIMES_TO_PLAY_SOUND

Use purpose:
Want to be notified when a file finishes downloading in Chrome
without specifying a file. Chrome creates a temporary download file
and renames it when the download completes.

Warning:
If used as import, initial_check and monitor functions utilize sys.exit().

"""

import os
from pygame import mixer
import sys
from time import sleep


def file_check(watchfile, cwd):
    if watchfile in os.listdir(cwd):
        return True
    else:
        return False


def play_sound(soundfile, soundplay):
    if soundplay:
        mixer.init()
        for x in range(soundplay):
            sound = mixer.Sound(soundfile)
            sound.play()
            while mixer.get_busy():
                sleep(0.5)


def initial_check(watchfile, cwd):
    if not file_check(watchfile, cwd):
        print("Terminating: File not found.")
        sys.exit()
    else:
        pass


def monitor(watchfile, cwd, soundfile, soundplay):
    while True:
        if file_check(watchfile, cwd):
            sleep(2)
        else:
            play_sound(soundfile, soundplay)
            print("File no longer found: " + watchfile)
            sys.exit()


if __name__ == '__main__':
    watchfile = sys.argv[1]
    soundplay = int(sys.argv[2])
    cwd = os.getcwd()
    soundfile = "/usr/share/sounds/KDE-K3B-Finish-Success.ogg"
    initial_check(watchfile, cwd)
    monitor(watchfile, cwd, soundfile, soundplay)
