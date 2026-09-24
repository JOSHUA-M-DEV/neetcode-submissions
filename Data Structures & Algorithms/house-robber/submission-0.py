class Solution:
    def fun(self,i,arr,dp):
        if i>=len(arr):
            return 0
        if dp[i]!=-1:
            return dp[i]
        dp[i]=max(arr[i]+self.fun(i+2,arr,dp),self.fun(i+1,arr,dp))
        return dp[i]
        
             
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*(len(nums)+1)
        return self.fun(0,nums,dp)
        