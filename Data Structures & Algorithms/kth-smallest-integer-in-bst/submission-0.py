# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def fun(self,root,arr):
        if root==None:
            return
        self.fun(root.left,arr)
        arr.append(root.val)
        self.fun(root.right,arr)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        self.fun(root,arr)
        return arr[k-1]
        