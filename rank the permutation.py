from itertools import permutations

s = "epwlz"


# l = sorted(s)
# ss = "".join(l)
# d = {}
# i=1
# for p in permutations(ss):
#
#     d[i]="".join(p)
#     i+=1
#
# for key, val in d.items():
#     if val == s:
#         print(key)
#         break

def factorial(s):
    if s == 0 or s == 1:
        return 1
    return s * factorial(s - 1)


#
# def findRank(s):
#     l = sorted(s)
#     ll = "".join(l)
#     #print(l)
#     checkList = [1] * (len(s))
#     #print(checkList)
#     ans = 0
#     indx = 0
#     for i in range(0, len(s)):
#         if checkList[i] == -1:
#             continue
#         elif s[indx] != ll[i]:
#             print(len(s) , indx , (len(s)-indx-1))
#             ans += factorial(len(s) - indx - 1)
#             print(ans)
#         else:
#             i = -1
#             indx += 1
#             checkList[i] = -1
#     return ans + 1

def findRank(s):
    smallerElements = []
    ans = 0
    for i in range(len(s)):
        count = 0
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                count += 1
        smallerElements.append(count)
    print(smallerElements)

    for i in range(len(s)):
        ans+=smallerElements[i]*factorial(len(s)-1-i)
    return ans+1





print(findRank(s))
