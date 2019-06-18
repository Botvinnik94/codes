#!/usr/bin/python3

import math
import sys

if len(sys.argv) != 2:
    print("Usage: <miller-rabin.py> <integer>")
    sys.exit()

n = int(sys.argv[1])
s = 0
t = 0

if n % 2 == 0:
    print("{0:d} no es primo".format(n))
    sys.exit()

#Descomposicion del numero en 1+2^s*t
temp = n - 1
while temp % 2 == 0:
    temp /= 2
    s += 1
t = int(temp)

print("Descomposicion: n=1+2^{0:d}*{1:d}".format(s, t))

#Eleccion de a para el algoritmo (deberia ser random, pero comenzamos desde lo mas bajo)
a = 2
temp_a = (a**t) % n
i = 0
r = 10

print("Prueba inicial a^t: {0:d}".format(temp_a))
#Test de decision
if temp_a == 1 or temp_a == n-1:
    print("{0:d} pasa el test".format(n))
    sys.exit()

else:
    while i < r:
        temp_a = (temp_a**2) % n
        print("Iteracion {0:d}: {1:d}".format(i, temp_a))
        if temp_a == n-1:
            print("{0:d} pasa el test".format(n))
            sys.exit()
        elif temp_a == 1:
            print("{0:d} no es primo".format(n))
            sys.exit()
        else:
            i += 1

print("{0:d} no es primo".format(n))