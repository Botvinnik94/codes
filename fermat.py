#!/usr/bin/python3

import sys
import math

if len(sys.argv) != 2:
    print("Usage: <fermat.py> <integer>")
    sys.exit()

n = int(sys.argv[1])

sqrt_n = math.sqrt(n)

if (sqrt_n).is_integer():
    print("q1 = {0:d}, q2 = {1:d}".format(int(sqrt_n), int(sqrt_n)))
    sys.exit()

sqrt_n = math.ceil(sqrt_n)

r = 50
i = 0
m = 0

while i < r:
    m = math.sqrt((sqrt_n + i)**2 - n)
    print("Iteracion {0:d}: m = {1:f}".format(i, m))
    if (m).is_integer():
        print("q1 = {0:d}, q2 = {1:d}".format(int(sqrt_n + i + m), int(sqrt_n + i - m)))
        sys.exit()
    else:
        i += 1

print("{0:d} no ha sido posible factorizarlo".format(n))