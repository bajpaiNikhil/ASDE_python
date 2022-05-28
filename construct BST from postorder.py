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


def constructTreeUtils(post, postIndex, param, minIs, maxIs, size):
    if postIndex[0]<0:
        return None
    root = None
    if (key)



def constructTree(post ,  size):
    postIndex = [size-1]
    return constructTreeUtils(post , postIndex , post[postIndex[0]] , minIs , maxIs , size)
