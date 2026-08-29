# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# double ended queue 
#implemented by C 
# Queue is multithreading only
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #make this hierarchy with root
        # childreun should be
        # BSF
        if not root:
            return []
        # level by level
        # queue 
        if not root:
            return []

        result = []
        queue = deque([root])

        #treverse level
        while queue :
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result




        

