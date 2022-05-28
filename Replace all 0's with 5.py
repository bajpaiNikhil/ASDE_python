n = 10120

#  o/p = 1004  + 5* 10^2 + 5 * 10^1 ==>
s = ""
n = str(n)
print(n)
for i in range(len(n)):
    print(n[i])
    if(n[i]== "0"):
        s+="5"
    else :
        s+=n[i]
print(s)
