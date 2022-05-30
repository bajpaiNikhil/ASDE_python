# s = "hrqcvsvszpsjammdrw"
import sys
from queue import Queue

s = "aabc"
q = Queue()
r = ""
charCount = [0] * 26

for i in range(len(s)):
    q.put(s[i])
    charCount[ord(s[i]) - ord('a')] += 1
    while not q.empty():
        if charCount[ord(q.queue[0]) - ord("a")] > 1:
            # print(q.get())
            q.get()
        else:
            r+=q.queue[0]
            break
    if q.empty():
        r+="#"
print(r)
print(charCount)
print(q.queue)
"""
hrqcvsvszhsjammdrw --> hhhhhhhhh#sssssss
hhhhhhhhhhhhhhhhhh
hrqcvs##zp#jam#d#w
"""
