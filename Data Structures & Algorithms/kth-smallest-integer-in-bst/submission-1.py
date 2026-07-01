# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = 0
        def dfs(root):
            if root == None:
                return
            nonlocal count
            nonlocal result
            dfs(root.left)
            count+=1
            if count == k:
                result = root.val
            dfs(root.right)
        
        dfs(root)
        print(count)
        return result