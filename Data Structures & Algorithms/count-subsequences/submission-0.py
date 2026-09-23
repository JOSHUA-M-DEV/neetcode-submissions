class Solution:
    
    def fun(self,i,j,s,t,dp):
        if j==len(t):
           
            return 1
        if i==len(s):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]

        p=0
        np=0
        if s[i]==t[j]:
            p+=self.fun(i+1,j+1,s,t,dp)
        np+=self.fun(i+1,j,s,t,dp)
        dp[i][j]=p+np
        return dp[i][j]
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[-1]*(len(t)+1) for _ in range(len(s))]
        return self.fun(0,0,s,t,dp)