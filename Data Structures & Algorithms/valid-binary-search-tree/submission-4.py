# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    def fun(self,root,l,h):
        if root==None:
            return True
        if root.val<=l or root.val>=h:
            return False
        return self.fun(root.left,l,root.val)and self.fun(root.right,root.val,h)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.fun(root,float('-inf'),float("inf"))
        

        