# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    from collections import deque
    # Encodes a tree to a single string.
    # anyway it's stacking [1,2,3,#,#,4,5]
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            if not node:
                result.append("#")
                return 
            #preorder
            # root left right
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # not it's string

        vals = data.split(",")
        self.i = 0

        def dfs():
            if self.i >= len(vals) or vals[self.i] == "#":
                self.i += 1
                return None
            root = TreeNode(int(vals[self.i]))
            self.i +=1

            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()
        
