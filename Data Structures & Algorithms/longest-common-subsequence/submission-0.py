class Solution:
    def fun(self,i,j,s1,s2,dp):
        if i<0 or j<0:
            return 0
        if s1[i]==s2[j]:
            return 1+self.fun(i-1,j-1,s1,s2,dp)
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j]=max(self.fun(i-1,j,s1,s2,dp),self.fun(i,j-1,s1,s2,dp))
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1]*len(text2) for _ in range(len(text1))]
        return self.fun(len(text1)-1,len(text2)-1,text1,text2,dp)
        