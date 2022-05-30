mat1 = [[1,5,6] , [8,10,11] , [15,16,18]]
mat2 = [[2,4,7] , [9,10,12] , [13,16,20]]

hashSet = set()
count = 0
target = 21

for i in range(len(mat2)):
    for j in range(len(mat2[0])):
        hashSet.add(mat2[i][j])
print(hashSet)

for row in range(len(mat1)):
    for col in range(len(mat1[0])):
        d = target-mat1[row][col]
        if d in hashSet:
            count+=1
print(count)

