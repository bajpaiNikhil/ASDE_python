
str1 = "azzxxzy"
stack = []

for i in range(len(str1)):
    if  len(stack) == 0 or str1[i] != stack[-1]:
        stack.append(str1[i])
    else:
        stack.pop()
print(stack)

