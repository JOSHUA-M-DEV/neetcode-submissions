class Solution:
    def fun(self,i,arr,k,dp):
        if i==len(arr):
            return 10**6
        if k==0:
            return 0
        p=10**6
        if (i,k) in dp:
            return dp[(i,k)]
        if arr[i]<=k:
            p=1+self.fun(i,arr,k-arr[i],dp)
        np=self.fun(i+1,arr,k,dp)
        dp[(i,k)]=min(p,np)
        return dp[(i,k)]
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        a=self.fun(0,coins,amount,dp)
        if a==10**6:
            return -1
        return a
        