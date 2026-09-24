class Solution:
    def fun(self,i,s,word,dp):
        if i==len(s):
            return True
        if dp[i]!=-1:
            return dp[i]
        for j in range(i+1,len(s)+1):
           
            if s[i:j] in word and self.fun(j,s,word,dp):
                dp[i]=True
                return dp[i]
        dp[i]=False
        return dp[i]


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        w=set(wordDict)
        dp=[-1]*(1+len(s))
        return self.fun(0,s,w,dp)
        