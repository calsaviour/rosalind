#!/usr/bin/python

import sys

def main(argv):

    print argv
    a = int(argv[0])
    b = int(argv[1])

    print a
    print b

    sumOfOddNumbers = 0
    while a<=b:
        if a % 2 !=0:
            sumOfOddNumbers+=a
        a=a+1
    print sumOfOddNumbers


if __name__ == "__main__":
   main(sys.argv[1:])
