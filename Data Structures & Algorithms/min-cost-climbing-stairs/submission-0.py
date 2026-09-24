class Solution:
    def fun(self,n,dp,arr):
        if n<0:
            return 0
        
        if dp[n]!=-1:
            return dp[n]
        dp[n]=arr[n]+min(self.fun(n-1,dp,arr),self.fun(n-2,dp,arr))
        return dp[n]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[-1]*(len(cost)+1)
        return min(self.fun(len(cost)-1,dp,cost),self.fun(len(cost)-2,dp,cost))
        