class Solution:
    def fun(self,i,nums,l,s):
        if i>=len(nums):
            s.append(l.copy())
            return
        l.append(nums[i])
        self.fun(i+1,nums,l,s)
        l.pop()
        self.fun(i+1,nums,l,s)

        
            

            
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s=[]
        l=[]
       
        self.fun(0,nums,l,s)
        
        return s
        