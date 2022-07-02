class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def lengthLinkedList(head):
    if head is None:
        return 0
    count = 1
    while head.next is not None:
        count += 1
        head = head.next
    return count

def findElementAtN(head , element):
    if head is None:
        return 0
    count = 1
    while head.next is not None :
        count+=1
        if count==element:
            return head.val
        head= head.next
    return 0

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)



n = 2
print(lengthLinkedList(head))
element = lengthLinkedList(head)+1
print(findElementAtN(head , element-n + 1))
