import sys
class TreeNode:
    def __init__(self , value , left=None , right=None):
        self.left = left
        self.right = right
        self.val = value


postOrder = [1, 7, 5, 50, 40, 10]
size = len(postOrder)

maxIs = sys.maxsize
minIs = -sys.maxsize
print(maxIs , minIs)


def constructTreeUtils(post, postIndex, key, minIs, maxIs, size):
    if postIndex[0]<0:
        return None
    root = None
    if minIs < key < maxIs:
        root = TreeNode(key)
        postIndex[0] = postOrder[0]-1
        if postIndex[0]>= 0:
            root.right = constructTreeUtils(post , postIndex , post[postIndex[0]] ,key ,maxIs , size )
            root.left = constructTreeUtils(post, postIndex, post[postIndex[0]], minIs, key, size)
    return root

def constructTree(post ,  size):
    postIndex = [size-1]
    return constructTreeUtils(post , postIndex , post[postIndex[0]] , minIs , maxIs , size)


print(constructTree(postOrder , size))