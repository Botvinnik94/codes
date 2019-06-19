import math
import sys
from random import randint

if len(sys.argv) != 4:
    print("Usage: <elgamal.py> <p> <g> <m>")
    sys.exit()

p = int(sys.argv[1])
g = int(sys.argv[2])
m = int(sys.argv[3])

da = randint(0,p-1)
db = randint(0,p-1)

ea = g**da%p
eb = g**db%p

k = randint(2, p-1)

print("A: da={0:d}, ea={1:d}, k={2:d}".format(da, ea, k))
print("B: db={0:d}, eb={1:d}".format(db, eb))

x = g**k%p
y = m*(eb**k)%p

print("A envia a B: (x = g^k, y = m * e^k) = ({0:d}, {1:d})".format(x, y))

m_des = y*((x**db)**(p-2))%p
print("B desencripta el mensaje y*((x^d)^-1): {0:d}".format(m_des))