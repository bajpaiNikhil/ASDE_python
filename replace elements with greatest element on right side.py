arr = [17, 18, 5, 4, 6, 1]

size = len(arr)
next_greater = arr[size - 1]
print(next_greater)
arr[size - 1] = -1
for i in range(size - 2, -1, -1):
    print(arr[i] ,i , arr)
    temp = arr[i]
    arr[i] = next_greater
    if next_greater < temp:
        print(temp , next_greater)
        next_greater = temp
print(arr)
