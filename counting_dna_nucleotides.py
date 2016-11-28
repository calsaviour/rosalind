#!/usr/bin/python

import sys

d={}

def main(argv):
    f = open(argv[0],'r')
    for line in f:
        return line.count("A"), line.count("G"), line.count("C"), line.count("T")



if __name__ == '__main__':
    print main(sys.argv[1:])
