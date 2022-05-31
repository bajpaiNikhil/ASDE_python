class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leftPathSum(root, sum):

    if root is None:
        return 0
    elif root.val == sum and root.left is None and root.right is None:
        return 1
    else:
        s = sum - root.val
        return leftPathSum(root.left, s) or leftPathSum(root.right, s)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

sum = 4
print(leftPathSum(root, sum))
