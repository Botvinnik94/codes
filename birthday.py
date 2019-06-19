import sys
import math

mod = 19683
m = 8748
c = 17801
i = 0
j = 0

while i < m:
    while j < m:
        if (c**i)%mod == (c**j)%mod and i != j:
            print("i={0:d}, j={1:d}, i-j={2:d}".format(i, j, (i-j)%m))
        j += 1
    i += 1
    j = 0
