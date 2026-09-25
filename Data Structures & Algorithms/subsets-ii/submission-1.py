class Solution:
    def fun(self,i,nums,l,s):
        
        s.append(l.copy())
           
        for j in range(i,len(nums)):
            if j>i and nums[j]==nums[j-1]:
                continue
            l.append(nums[j])
            self.fun(j+1,nums,l,s)
            l.pop()

        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s=[]
        l=[]
        nums.sort()
        self.fun(0,nums,l,s)
        
        return s
        