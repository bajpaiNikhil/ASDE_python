arr = [1, 3, 5, 4]
size = len(arr)
arr.sort()

auxArr = [0] * 5
mid = (size - 1) // 2

auxArr[mid] = arr[0]
print(arr , auxArr , mid , auxArr[mid])

i = 1
inputArrayIndex = 1
for i in range(1, mid + 1):
    print(auxArr , i ,arr[i] , inputArrayIndex , arr[inputArrayIndex])
    auxArr[mid + i] = arr[inputArrayIndex]
    inputArrayIndex += 1
    print(auxArr)
    auxArr[mid - i] = arr[inputArrayIndex]
    inputArrayIndex += 1
    print(auxArr)
print(i, inputArrayIndex)
if size % 2 == 0:
    auxArr[-1] = max(arr)
print(auxArr)
