# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #DFS
        #go down, if node.val > 0 : save
        # elif not save
        #return max_path_sum
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0

            left_gain = max(0,dfs(node.left))
            right_gain = max(0,dfs(node.right))

            current_path = node.val+ left_gain + right_gain
            max_sum = max(max_sum , current_path)

            return node.val + max(left_gain,right_gain)

        dfs(root)
        return max_sum        

