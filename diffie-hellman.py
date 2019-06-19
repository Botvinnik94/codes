import math
import sys
from random import randint

if len(sys.argv) != 3:
    print("Usage: <diffie-hellman.py> <p> <g>")
    sys.exit()

p = int(sys.argv[1])
g = int(sys.argv[2])


da = randint(0, p-1)
db = randint(0, p-1)

ea = g**da%p
eb = g**db%p

print("A: da={0:d}, ea={1:d}".format(da, ea))
print("B: db={0:d}, eb={1:d}".format(db, eb))

k = g**(da*db)%p

print("K = g^(da*db) = {0:d}".format(k))