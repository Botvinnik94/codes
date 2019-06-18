#!/usr/bin/python3

import sys
import math


def euclides(a, b):
    r0 = a
    r1 = b
    i = 1
    while r1 != 0:
        temp = r1
        r1 = r0 % r1
        #print("i={0:d}\tr0={1:d}\tr1={2:d}\tr2={3:d}".format(i, r0, temp, r1))
        r0 = temp
        i += 1

    return r0

def main(argv):
    if len(argv) != 3:
        print("Usage: <euclides.py> <a> <b>")
        sys.exit()

    a = int(argv[1])
    b = int(argv[2])

    print(euclides(a, b))

if __name__ == "__main__":
    main(sys.argv)
