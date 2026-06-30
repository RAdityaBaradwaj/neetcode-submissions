# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = []
        result = []

        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.pop(0)
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            
            if level:
                result.append(level)
        answer = []
        for l in result:
            answer.append(l[-1])
        
        return answer