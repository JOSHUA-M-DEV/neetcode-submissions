class Solution:
    def fun(self,i,arr,k,dp):
        if len(arr)==i:
            if k==0:
                return 1
            return 0
        if k==0:
            return 1
        if dp[i][k]!=-1:
            return dp[i][k]
        p=0
        if arr[i]<=k:
            p=self.fun(i,arr,k-arr[i],dp)
        dp[i][k]=p+self.fun(i+1,arr,k,dp)
        return dp[i][k]
            

    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[-1]*(amount+1) for _ in range(len(coins))]
        return self.fun(0,coins,amount,dp)
        