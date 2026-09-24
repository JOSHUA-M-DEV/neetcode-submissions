class Solution:
    def fun(self,i,j,s,p,dp):
        if j==len(p):
            return i==len(s)
        if (i,j) in dp:
            return dp[(i,j)]
        match= i<len(s) and (s[i]==p[j] or p[j]=='.')
        if (j+1)<len(p) and p[j+1]=='*':
            dp[(i,j)]=self.fun(i,j+2,s,p,dp) or (match and self.fun(i+1,j,s,p,dp))
            return dp[(i,j)]
        if match:
            dp[(i,j)]=self.fun(i+1,j+1,s,p,dp)
            return dp[(i,j)]
        dp[(i,j)]=False
        return dp[(i,j)]



    def isMatch(self, s: str, p: str) -> bool:
        dp={}
        return self.fun(0,0,s,p,dp)

        