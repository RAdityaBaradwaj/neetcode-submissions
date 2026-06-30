# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def goodNode(root, maxval):
            if root == None:
                return
            nonlocal count
            if root.val >= maxval:
                count +=1
                maxval = root.val
            goodNode(root.left,maxval)
            goodNode(root.right,maxval)

        goodNode(root,-float('inf'))

        return count
