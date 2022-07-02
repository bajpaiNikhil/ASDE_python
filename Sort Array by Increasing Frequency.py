
from collections import defaultdict
from  collections import  Counter
nums = [-1,1,-6,4,5,-6,1,4,1]

hashMap = Counter(nums).most_common()
print(hashMap)
hashMap.sort(key = lambda x: x[0], reverse=True)
hashMap.sort(key = lambda x:x[1])
print(hashMap)
l = []
for i in hashMap:
    print(i)
    a,b = i

    l.extend([a]*b)
print(l)