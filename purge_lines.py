'''Purge lines containing string
Usage:
  script [filename] "string to purge"
'''
import sys


def purge(filename, the_string):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    f = open(filename, 'w')

    i = 0

    for line in lines:
        i =+ 1
        if the_string in line:
            print filename, ": ", line
        else:
            f.write(line)

    f.close()


if __name__ == '__main__':
    filename = sys.argv[1]
    the_string = sys.argv[2]
    purge(filename, the_string)
