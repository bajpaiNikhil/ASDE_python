import math
import sys

arr1 = [10, 19, 18]
arr2 = [11, 15, 9]

for i in range(len(arr1)):
    if arr1[i] == 1:
        arr1[i]=sys.maxsize
    else:
        arr1[i]=arr1[i]/(math.log(arr1[i]))
arr1.sort()
print(arr1)
for j in range(len(arr2)):
    if arr2[j] == 1:
        arr2[j]=sys.maxsize
    else:
        arr2[j] = arr2[j]/(math.log(arr2[j]))
arr2.sort()
print(arr2)

pointA = 0
pointB = 0
count = 0
while pointA < len(arr1) and pointB < len(arr2):
    if arr1[pointA] < arr2[pointB]:
        count +=len(arr2)-pointB
        pointA+=1
    else:
        pointB+=1
print(count)
