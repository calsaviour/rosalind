#!/usr/bin/python

import sys
import re

d = {}

def main(agrv):
    f = open('dictionary_text.txt')
    for line in f:
        line = line.replace('\n', '')
        for word in line.split(' '):
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1

    f.close()


if __name__ == "__main__":
   main(sys.argv[1:])

   for key, value in d.items():
       print '{} {}'.format(key, value)
