class Solution:
    def fun(self,i,j,arr,dp):
        if j>=len(arr):
            return 0
        if i>j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        p=0
        if i==-1 or arr[i]<arr[j]:
            p=1+self.fun(j,j+1,arr,dp)

        np=self.fun(i,j+1,arr,dp)
        dp[i][j]=max(p,np)
        return dp[i][j]
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[[-1]*(len(nums)+1) for _ in range(len(nums))]
        return self.fun(-1,0,nums,dp)

        