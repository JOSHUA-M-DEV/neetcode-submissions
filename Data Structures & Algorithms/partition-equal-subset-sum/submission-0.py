class Solution:
    def fun(self,i,nums,t,dp):
        if i==len(nums):
            return False
        if t==0:
            return True
        if (i,t) in dp:
            return dp[(i,t)]
        p=False
        if nums[i]<=t:
            p=self.fun(i+1,nums,t-nums[i],dp)
        np=self.fun(i+1,nums,t,dp)
        dp[(i,t)]=p or np
        return dp[(i,t)]
        
            
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        dp={}
        if s%2==1:
            return False
        return self.fun(0,nums,s//2,dp)
        