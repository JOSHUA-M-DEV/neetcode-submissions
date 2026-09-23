class Solution:
    def fun(self,i,j,arr,dp):
        if i>=len(arr):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        
        if j==0:
            dp[i][j]=max(-arr[i]+self.fun(i+1,1,arr,dp),self.fun(i+1,0,arr,dp))
        np=0
        if j==1:
            dp[i][j]=max(arr[i]+self.fun(i+2,0,arr,dp),self.fun(i+1,1,arr,dp))
        
        return dp[i][j]

    def maxProfit(self, prices: List[int]) -> int:
        dp=[[-1]*3 for _ in range(len(prices))]
        return self.fun(0,0,prices,dp)
        