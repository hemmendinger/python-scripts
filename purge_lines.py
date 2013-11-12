'''Purge lines containing string (case insensitive)
Usage:
  script [filename] "string to purge"
'''
import sys


def purge(filename, the_string):
    the_string = the_string.lower()
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    f = open(filename, 'w')
    i = 0
    found = False
    for line in lines:
        i += 1
        if the_string in line.lower():
            print filename,":" ,i ,": " ,line
            found = True
        else:
            f.write(line)
    if found == False:
        print "No matches found"
    f.close()

if __name__ == '__main__':
    filename = sys.argv[1]
    the_string = sys.argv[2]
    purge(filename, the_string)
