# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isVBST(root):
            if root == None:
                return True, -1001, 1001
            if root.right == None and root.left == None:
                return True, root.val, root.val
            
            isRightBST, maxRightVal, minRightVal = isVBST(root.right)
            isLeftBST, maxLeftVal, minLeftVal = isVBST(root.left) 
            if not isRightBST or not isLeftBST:
                return False, maxLeftVal, minRightVal
            elif minRightVal <= root.val or maxLeftVal >= root.val:
                return False, maxLeftVal, minRightVal
            else:
                return True, max(maxRightVal,root.val), min(minLeftVal,root.val)
        
        isBST, minVal, maxVal = isVBST(root)

        return isBST

