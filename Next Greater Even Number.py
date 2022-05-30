x =  275353939
# //333557992
x = list(str(x))
print(x)


# print(x)


# 34722641 --> 3472 2 64 1 --> 3472 4 62 1 --> 3472 4 12 6

# x = str(x)
def nextGreatestEvenNumber(x):
    n = len(x)
    if n==1 :
        return -1
    i = 1
    for i in range(n - 1, 0, -1):
        # print(x[i])
        if x[i] > x[i - 1]:
            break
    # print(i, x[i], x[i - 1])

    if i == 1 and x[i] <= x[i - 1]:
        return -1
    num = x[i - 1]
    smallest = i
    for j in range(i + 1, n):
        if num < x[j] < x[smallest]:
            #print(num , x[j] , x[smallest])
            smallest = j
            # print(smallest, x[smallest])
    #print(x[smallest], num)

    x[smallest], x[i - 1] = x[i - 1], x[smallest]
    x = x[:i] + sorted(x[i:])
    #print(x)
    if int(x[-1]) % 2 != 0:
        print(int("".join(x)))
        return nextGreatestEvenNumber(x)
    else:
        return int("".join(x))


# def checkForLastEven(x)

print(nextGreatestEvenNumber(x))
