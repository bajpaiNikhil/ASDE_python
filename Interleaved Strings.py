from collections import  Counter
a = "XY"
b = "X"
c ="XXY"

d = dict(Counter(a+b))
print(d)

for i in c:
    if i in d:
        d[i]-=1
for key,val in d.items():
    if val!=0:
        print(0)
        break
print(1)