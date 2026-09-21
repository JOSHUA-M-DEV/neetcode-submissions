# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def fun(self,root,m):
        if root==None:
            return 0
        r=0
        if root.val>=m:
            r=1
        m=max(m,root.val)
        r+=self.fun(root.left,m)
        r+=self.fun(root.right,m)
        return r
    def goodNodes(self, root: TreeNode) -> int:
        return self.fun(root,root.val)
        
            


        