import sys
import math
import numpy

if len(sys.argv) != 4:
    print("Usage: <bsgs.py> <prime modulus> <g> <a>")
    sys.exit()

p = int(sys.argv[1])
g = int(sys.argv[2])
a = int(sys.argv[3])

m = math.floor(math.sqrt(p))

i=0
j=1
table_j = {}

#exp = numpy.int64((g**(p-2))%p)
#table_j[a] = 0
#print("j: {0:d}\t\ta*g^-j: {1:d}".format(0, a))
#prev = a
while j<=m:
    #temp = numpy.int64(prev*exp % p)
    temp = numpy.int64(g**j)
    table_j[temp] = j
    print("j: {0:d}\t\ta*g^-j: {1:d}".format(j, temp))
    #prev = temp
    j += 1    

print("")

while i<p:
    temp = numpy.int64((g**(i*m)) % p)
    print("i: {0:d}\t\tg^(im): {1:d}".format(i, temp))
    if temp in table_j:
        j = table_j[temp]
        print("\ni={0:d}, j={1:d}, n={2:d}".format(i, j, 5*m + j))
        sys.exit()
    i += 1


