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
        l=max(0,self.fun(root.left,m))
        r=max(0,self.fun(root.right,m))
        m[0]=max(m[0],l+r+root.val)
        return root.val+max(l,r)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        m=[float("-inf")]
        self.fun(root,m)
        return m[0]

        