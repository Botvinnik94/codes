import numpy
import sys
import math

if len(sys.argv) != 3:
    print("Usage: <polydiv.py> <dividendo> <divisor> (Operandos en forma vectorial)")
    sys.exit()

dividendo = list(sys.argv[1])
divisor = list(sys.argv[2])
dividendo = list(map(int, dividendo))
divisor = list(map(int, divisor))
print(numpy.polydiv(dividendo, divisor))