# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.m=0
        def fun(r):
            if r==None:
                return 0
            l1=fun(r.left)
            r1=fun(r.right)
            self.m=max(self.m,l1+r1)
            print(self.m)
            return 1+max(l1,r1)
        fun(root)
        return self.m


        