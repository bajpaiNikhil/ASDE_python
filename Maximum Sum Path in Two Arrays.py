arr1 = [2, 4, 5, 8, 10]
arr2 = [4, 6, 8, 9]

lengthArr1 = len(arr1)
lengthArr2 = len(arr2)


def maximumSumPathArray(arr1, arr2, lengthArr1, lengthArr2):
    i = 0
    j = 0
    sum1 = 0
    sum2 = 0
    result = 0
    while i < lengthArr1 and j < lengthArr2:
        if arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            sum2 += arr2[j]
            j += 1
        else:
            result += max(sum1, sum2) + arr1[i]
            sum2 = 0
            sum1 = 0
            j += 1
            i += 1
    if i < lengthArr1:
        sum1 += sum(arr1[i:])
    if j < lengthArr2:
        sum2 += sum(arr2[j:])
    result += max(sum1, sum2)
    return result


print(maximumSumPathArray(arr1, arr2, lengthArr1, lengthArr2))
