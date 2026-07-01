# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxValue = -float('inf')

        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal maxValue
            maxValue = max(maxValue, left+right+root.val, left+root.val, right+root.val,root.val)

            return max(left+root.val,right+root.val,root.val)

        dfs(root)
        return maxValue