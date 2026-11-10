class Solution:
    
    def fun(self,i,s,dp):
        if i in dp:
            return dp[i]
        
        if s[i]=='0':
            return 0

        way=self.fun(i+1,s,dp)
        
        if (i+1)<len(s) and 10<=int(s[i:i+2])<=26:
            way+=self.fun(i+2,s,dp)
        dp[i]=way
        return dp[i]
    
        
        

        

    def numDecodings(self, s: str) -> int:
        dp={len(s):1}
        
        return self.fun(0,s,dp)


        