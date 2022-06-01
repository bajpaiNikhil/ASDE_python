import math
from functools import reduce

n = 11
k = n
t = 9
l = []
N = n
while t > 1:
    if n % t == 0:
        l.append(t)
        n //= t
    else:
        t-=1
if len(l)>0:

    result = reduce((lambda x, y: x * y), l)
    l.sort()
    print("".join(list(map(str , l))))
else:
    print("No")
