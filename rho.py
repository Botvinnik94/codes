#!/usr/bin/python3

import sys
import math
import numpy
from euclides import euclides


def calculatePoint(fx, i, n, original):
    if i == 0:
        return numpy.int64(numpy.polyval(fx, 1)) % n
    elif original == 0:
        prev = calculatePoint(fx, i-1, n, 0)
        return numpy.int64(numpy.polyval(fx, prev)) % n
    else:
        return calculatePoint(fx, i-1, n, 0)


def main(argv):
    if len(argv) != 2:
        print("Usage: <rho.py> <integer>")
        sys.exit()

    n = int(argv[1])


    i = 1
    r = 100
    while i < r:
        ai = calculatePoint([1, 0, 1], i, n, 1)
        a2i = calculatePoint([1, 0, 1], i*2, n, 1)
        mcd = euclides((a2i - ai) % n, n) 

        print("i = {0:d}\t\tai = {1:d}\t\ta2i = {2:d}\t\tmcd(a2i - ai, n) = {3:d}".format(i, ai, a2i, mcd))

        if mcd == 1:
            i += 1
        elif mcd == n:
            print("{0:d} fallo al factorizar".format(n))
            sys.exit()
        else:
            q1 = mcd
            q2 = n / mcd
            print("q1 = {0:d}, q2 = {1:d}".format(int(q1), int(q2)))
            sys.exit()
    
    print("{0:d} fallo al factorizar".format(n))



if __name__ == "__main__":
    main(sys.argv)
