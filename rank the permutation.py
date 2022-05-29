
from itertools import  permutations
s = "string"
l = sorted(s)
ss = "".join(l)
d = {}
i=1
for p in permutations(ss):

    d[i]="".join(p)
    i+=1

for key, val in d.items():
    if val == s:
        print(key)
        break

