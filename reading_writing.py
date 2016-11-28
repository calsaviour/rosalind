#!/usr/bin/python

import sys

def main(argv):
    filename = argv[0]
    f = open(filename,'r')
    index = 1
    outputtext = ''
    for line in f:
        if index % 2 == 0:
            outputtext = outputtext + line
        index = index + 1
    f.close()
    output  = open('output.txt','w')
    output.write(outputtext)
    output.close()

if __name__ == "__main__":
   main(sys.argv[1:])
