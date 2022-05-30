

class TreeNode:
    def __init__(self , val ,left = None , right = None):
        self.val =  val
        self.left = left
        self.right = right


def sumTree(root):
    if root == None:
        return 0
    oldVal = root.val

    root.val = sumTree(root.left) + sumTree(root.right)
    return oldVal + root.val

root = TreeNode(10)
root.left = TreeNode(-2)
root.left.left = TreeNode(8)
root.left.right = TreeNode(-4)
root.right = TreeNode(6)
root.right.right = TreeNode(5)
root.right.left = TreeNode(7)

print(sumTree(root))
