x  = [3, 2, 1]


def nextGreatestEvenNumber(x):
    n = len(x)
    a = sorted(x , reverse=True)
    #print(a , x)
    if x == a:
        return sorted(x)
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
    return x


# def checkForLastEven(x)

print(nextGreatestEvenNumber(x))
