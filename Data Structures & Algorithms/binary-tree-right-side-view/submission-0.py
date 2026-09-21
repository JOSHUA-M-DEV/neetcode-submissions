# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def fun(self,i,arr,root):
        if root==None:
            return
        if i==len(arr):
            arr.append(root.val)
        self.fun(i+1,arr,root.right)
        self.fun(i+1,arr,root.left)
        

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        self.fun(0,arr,root)
        return arr
        