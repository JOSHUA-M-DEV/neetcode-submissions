class Solution:
    def fun(self,i,j,arr,dp):
        if i>j:
            return 0
        if dp[i]!=-1:
            return dp[i]
        dp[i]=max(arr[i]+self.fun(i+2,j,arr,dp),self.fun(i+1,j,arr,dp))
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp=[-1]*(len(nums)+1)
        dp1=[-1]*(len(nums)+1)

        return max(self.fun(0,len(nums)-2,nums,dp),self.fun(1,len(nums)-1,nums,dp1))
        