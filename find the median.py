


arr = [56 ,67 ,30 ,79]
arr.sort()

print(arr)
n = len(arr)
print((arr[(n//2)+1] + arr[n//2]) ,arr[(n//2)-1] ,arr[n//2]  )
s = (arr[(n//2)-1] + arr[n//2])//2
print(s)