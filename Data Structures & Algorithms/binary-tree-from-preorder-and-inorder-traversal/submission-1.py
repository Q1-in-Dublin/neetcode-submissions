# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #efficient index finding ? dictionary
        inorder_map = {val:idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0

        def array_to_tree(in_left: int,in_right:int):
            if in_left > in_right:
                return None

            # pre_idx's [0] is root
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            # this is index can +1
            
            self.pre_idx += 1
            mid = inorder_map[root_val]

            root.left = array_to_tree(in_left, mid-1)
            root.right = array_to_tree(mid+1, in_right)
            return root
        return array_to_tree(0, len(inorder)-1)



        # preorder[0] is root node
        # divide into root and left children right children
        # if not preorder or not inorder:
        #     return None

        # root_val = preorder[0]
        # root = TreeNode(root_val)
        # mid = inorder.index(root_val)
        # # 1 is the root_val and until mid
        # root.left = self.buildTree(preorder[1: 1+mid],inorder[:mid])
        # # 1~ mid and next from that , 1+ mid to the end
        # root.right = self.buildTree(preorder[1+mid:], inorder[mid+1 :])

        # return root