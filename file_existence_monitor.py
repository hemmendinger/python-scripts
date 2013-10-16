'''
Notify if files in a directory have changed, but only by file names.

Usage:
python script.py FILENAME_TO_WATCH NUMBER_OF_TIMES_TO_PLAY_SOUND

Use purpose:
Want to be notified when a file finishes downloading in Chrome
without specifying a file. Chrome creates a temporary download file
and renames it when the download completes.

'''

import os, sys, pygame
from time import sleep


def file_check(watchfile, cwd):
    if watchfile in os.listdir(cwd):
        return True
    else:
        return False


def play_sound(soundfile, soundplay):
    if soundplay:
        pygame.mixer.init()
        for x in range(soundplay):
            sound = pygame.mixer.Sound(soundfile)
            sound.play()
            while pygame.mixer.get_busy():
                sleep(0.5)


def initial_check(watchfile, cwd):
    if file_check(watchfile, cwd) == False:
        print("Terminating: File not found.")
        sys.exit()
    else:
        exists = True


def monitor(watchfile, cwd, soundfile, soundplay):
    while True:
        if file_check(file, cwd):
            sleep(2)
        else:
            play_sound(soundfile, soundplay)
            print("File no longer found: " + file)
            sys.exit()


if __name__ == '__main__':
    watchfile = sys.argv[1]
    soundplay = int(sys.argv[2])
    cwd = os.getcwd()
    soundfile = "/usr/share/sounds/KDE-K3B-Finish-Success.ogg"
    initial_check(file, cwd)
    monitor(file, cwd, soundfile, soundplay)
