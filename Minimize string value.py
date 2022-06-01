from queue import PriorityQueue

s = "bcaebbbec"
k = 5


frequencyMap = [0] * 256

for i in s:
    frequencyMap[ord(i)-ord("a")] +=1
print(frequencyMap)

priorityQueue = PriorityQueue()

for i in range(0 , 256):
    priorityQueue.put(-frequencyMap[i])
print(priorityQueue.queue)

while k >0:
    temp = priorityQueue.get()
    print(temp)
    temp+=1
    priorityQueue.put(temp , temp)
    print(priorityQueue.queue)
    k-=1
result = 0
while not priorityQueue.empty():
    temp = priorityQueue.get()
    # temp = temp*(-1)
    result += (temp * temp)
print(result)