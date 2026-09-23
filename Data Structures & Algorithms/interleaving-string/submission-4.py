class Solution:
    def fun(self,i,j,z,s1,s2,s3,dp):
        if z==len(s3):
            return j==len(s2) and i==len(s1)

        if dp[i][j][z]!=-1:
            return dp[i][j][z]
        
        if i<len(s1) and s1[i]==s3[z]:
            if self.fun(i+1,j,z+1,s1,s2,s3,dp):
                dp[i][j][z]=True
                return dp[i][j][z]
        if j<len(s2) and s2[j]==s3[z]:
            if self.fun(i,j+1,z+1,s1,s2,s3,dp):
                dp[i][j][z]=True

                return dp[i][j][z]
        dp[i][j][z]=False
        return dp[i][j][z]
        
        
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp=[[[-1]*(len(s3)+1)]*(1+len(s2)) for _ in range(len(s1)+1)]
        
        return self.fun(0,0,0,s1,s2,s3,dp)
        