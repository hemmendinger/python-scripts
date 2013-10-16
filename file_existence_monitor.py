import os, sys, pygame
from time import sleep

'''
Notify if files in a directory have changed, but only by file names.

Usage:
python script.py FILENAME_TO_WATCH INTEGER

Use purpose:
Want to be notified when a file finishes downloading in Chrome
ithout specifying a file. Chrome creates a temporary download file
and renames it when the download completes.

'''

file = sys.argv[1]
soundplay = int(sys.argv[2])
cwd = os.getcwd()
soundfile = "/usr/share/sounds/KDE-K3B-Finish-Success.ogg"


def file_check(file, cwd):
    if file in os.listdir(cwd):
        return True
    else:
        return False

def play_sound(soundfile, soundplay):
    sound = []
    if soundplay:
        pygame.mixer.init()
        for x in range(soundplay):
            sound = pygame.mixer.Sound(soundfile)
            sound.play()
            while pygame.mixer.get_busy():
                sleep(1)

def initial_check(file, cwd):
    if file_check(file, cwd) == False:
        print("Terminating: File not found.")
        sys.exit()
    else:
        exists = True

def monitor(file, cwd):
    while True:
        if file_check(file, cwd):
            sleep(5)
        else:
            play_sound(soundfile, soundplay)
            print("Temporary download file no longer found: " + file)
            sys.exit()

if __name__ == '__main__':
#    play_sound(soundfile, soundplay)
    initial_check(file, cwd)
    monitor(file, cwd)
