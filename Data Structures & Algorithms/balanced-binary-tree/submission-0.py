# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.m=0
        def fun(r):
            if r==None:
                return 0

            l1=fun(r.left)
            if l1==-1:
                return -1
            r1=fun(r.right)
            if r1==-1:
                return -1
            if abs(r1-l1)>1:
                return -1
            return 1+max(l1,r1)
        
        return fun(root)!=-1
        