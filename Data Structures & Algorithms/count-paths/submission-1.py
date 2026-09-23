class Solution:
    def fun(self,m,n,dp):
        if m<0 or n<0:
            return 0
        if m==0 and n==0:
            return 1
        if dp[m][n]!=-1:
            return dp[m][n]
        dp[m][n]=self.fun(m-1,n,dp)+self.fun(m,n-1,dp)
        return dp[m][n]
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*n for _ in range(m)]
        return self.fun(m-1,n-1,dp)
        