# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        answer = []
        queue.append(root)
        while len(queue):
            lenQ = len(queue)
            level = []
            for i in range(lenQ):
                root = queue.pop(0)
                if root:
                    level.append(root.val)
                    queue.append(root.left)
                    queue.append(root.right)
            if level:
                answer.append(level.pop())
        return answer
            


        
        return answer