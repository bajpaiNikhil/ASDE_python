arr = [1, 2, 3, -2, 5]

greatestSum = arr[0]
currentSum = arr[0]

for i in range(1, len(arr)):
    currentSum  = max(currentSum+arr[i] , arr[i])
    greatestSum = max(greatestSum, currentSum)
print(greatestSum)
