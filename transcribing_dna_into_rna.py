#!/usr/bin/python
import sys

def main(argv):
    f = open(argv[0],'r')
    for line in f:
        print line.replace('T','U')

if __name__ == '__main__':
    main(sys.argv[1:])
