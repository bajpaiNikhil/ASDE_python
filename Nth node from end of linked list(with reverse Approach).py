class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head):
    if not head or not head.next:
        return head






head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)


print(reverseLinkedList(head))