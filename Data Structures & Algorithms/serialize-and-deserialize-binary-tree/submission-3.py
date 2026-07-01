# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []

        def dfs(root):
            nonlocal preorder
            if root == None:
                preorder.append("N")
                return
            preorder.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return "$".join(str(n) for n in preorder)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = [x for x in data.split("$")]


        def dfs(preorder):
            if not preorder:
                return None
            if preorder[0] == "N":
                preorder.pop(0)
                return None
            root = TreeNode(int(preorder.pop(0)))
            root.left = dfs(preorder)
            root.right = dfs(preorder)

            return root

        return dfs(preorder)


