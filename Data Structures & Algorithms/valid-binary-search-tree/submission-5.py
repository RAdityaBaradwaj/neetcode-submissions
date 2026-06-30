# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode],minval=-float('inf'),maxval=float('inf')) -> bool:
        if root == None:
            return True
        
        if root.left and (root.left.val >= root.val or (root.left.val <= minval or root.left.val >= maxval)):
            return False
        if root.right and (root.right.val <= root.val or (root.right.val <= minval or root.right.val >= maxval)):
            return False
        return self.isValidBST(root.left,minval,root.val) and self.isValidBST(root.right,root.val,maxval)

