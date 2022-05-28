arr = [2,4,7,8,9,10]
size = len(arr)
mid = size//2

for i in range(0 , size-1, 2):
    print(i)
    arr[i] , arr[i+1] = arr[i+1] , arr[i]
print(arr)