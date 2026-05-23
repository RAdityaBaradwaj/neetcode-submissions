# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        gNodes = 0

        def dfs(root,maxVal):
            nonlocal gNodes
            if root == None:
                return
            if root.val >= maxVal:
                gNodes +=1
                dfs(root.right,root.val)
                dfs(root.left,root.val)
            else:
                dfs(root.right,maxVal)
                dfs(root.left,maxVal)
        
        dfs(root,-101)
        return gNodes