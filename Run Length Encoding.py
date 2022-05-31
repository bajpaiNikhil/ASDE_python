import collections
from collections import defaultdict

s = "abbbcdddd"
s +="0"
d = ""

count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        d+=s[i] + str(count)
        count=1
print(d)


#
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
#
# print(d.keys())
# print(d)
# r = ""
# for key , val in d.items():
#     print(key ,val)
#     r+=key+str(val)
# print(r)
