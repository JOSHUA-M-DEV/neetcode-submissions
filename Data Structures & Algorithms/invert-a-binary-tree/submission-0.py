# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def fun(self,root):
        if root==None:
            return
        
        root.right,root.left=root.left,root.right
        self.fun(root.right)
        self.fun(root.left)
        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.fun(root)
        return root
    
            

        