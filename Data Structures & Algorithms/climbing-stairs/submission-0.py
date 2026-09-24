class Solution:
    def fun(self,n,dp):
        if n<0:
            return 0
        if n==0:
            return 1
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.fun(n-1,dp)+self.fun(n-2,dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        return self.fun(n,dp)
        