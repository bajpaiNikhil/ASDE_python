arr = [8, 3, 1, 2]


def findPivot(arr):
    for i in range(len(arr)):
        if arr[i] > arr[(i + 1) % len(arr)]:
            return i


def rotatedSum(arr):
    sum = 0
    diff = len(arr) - 1 - findPivot(arr)
    for i in range(len(arr)):
        sum = sum + ((i + diff) % len(arr)) * arr[i]
    return sum


print(rotatedSum(arr))
