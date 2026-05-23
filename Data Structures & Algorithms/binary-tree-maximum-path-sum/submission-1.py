# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -1001
        def mps(root):
            nonlocal maxSum
            if root == None:
                return 0
            maxLeftSum = mps(root.left)
            maxRightSum = mps(root.right)
            print(root.val,maxLeftSum,maxRightSum)

            if maxLeftSum < 0 and maxRightSum < 0:
                maxSum = max(root.val,maxSum)
                return root.val
            elif maxLeftSum >= 0 and maxRightSum < 0:
                maxSum = max(root.val+maxLeftSum,maxSum)
                return root.val+maxLeftSum
            elif maxLeftSum < 0 and maxRightSum >= 0:
                maxSum = max(root.val+maxRightSum, maxSum)
                return root.val+maxRightSum
            else:
                maxSum = max(root.val + maxRightSum + maxLeftSum, maxSum)
                return root.val + max(maxLeftSum,maxRightSum)
        
        mps(root)
        return maxSum


        
