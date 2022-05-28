N = 4
Mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]
       ]

extraArray = []

print(*Mat[0])
for i in Mat:
       extraArray.extend(i)
print(extraArray)
extraArray.sort()
k=0
for i in range(N):
       for j in range(N):
              Mat[i][j] = extraArray[k]
              k+=1
print(Mat)