arr = [1,1,1,1]
k = 2

hashMap = {}
count=0
for i in range(len(arr)):
    diff = k-arr[i]
    if diff in hashMap:
        count+=hashMap[diff]
        hashMap[arr[i]] = hashMap.get(arr[i],0)+1
        print(hashMap , count)
    else:
        hashMap[arr[i]] = hashMap.get(arr[i], 0) + 1
print(count)

