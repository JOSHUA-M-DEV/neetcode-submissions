class Solution:
    def fun(self,i,j,s1,s2,dp):
        
        if i==len(s1):
            return len(s2)-j
        if j==len(s2):
            return len(s1)-i
        if dp[i][j]!=-1:
            return dp[i][j]
        if s1[i]==s2[j]:
            dp[i][j]=self.fun(i+1,j+1,s1,s2,dp)
            return dp[i][j]
        dp[i][j]=min(1+self.fun(i+1,j,s1,s2,dp),min(1+self.fun(i+1,j+1,s1,s2,dp),1+self.fun(i,j+1,s1,s2,dp)))
        return dp[i][j]
        

        

    def minDistance(self, word1: str, word2: str) -> int:
        
        dp=[[-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        return self.fun(0,0,word1,word2,dp)
        