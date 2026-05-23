# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        treeList = ""

        def dfs(root):
            nonlocal treeList
            if root != None:
                treeList+=str(root.val)+','
                dfs(root.left)
                dfs(root.right)
            else:
                treeList+='N,'
        
        dfs(root)

        return treeList
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dataList = data.split(',')

        i = 0
        print(dataList)
        def dfs():
            nonlocal dataList, i
            if dataList[i] == 'N':
                i+=1
                return None
            else:
                rootNow = TreeNode(int(dataList[i]))
                i+=1
                rootNow.left = dfs()
                rootNow.right = dfs()
                return rootNow
        
        return dfs()
        

