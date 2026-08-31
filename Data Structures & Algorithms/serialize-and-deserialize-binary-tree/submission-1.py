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
        if not root : 
            return ""
        
        result = []
        queue = deque([root])

        while queue :
            # pick one from left
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                # not node fill out with any sign
                result.append(str("#"))
        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # not it's string

        if not data :
            return None

        vals = data.split(",")

        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1
        while queue and i< len(vals):
            node = queue.popleft()

            #left children
            if vals[i] != "#":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i+=1
            
            # right children
            if i <len(vals) and vals[i] != "#":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i+= 1
        return root

        
