# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check if it is BST
        # ex1) yes
        # ex2) no 
        # O(n) worst case

        if not root :
            return None
        #using a recursive
        root.left,root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        
