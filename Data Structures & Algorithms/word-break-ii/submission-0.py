class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        h=set(wordDict)
        l=[]
        def dfs(i):
            if i==len(s):
                res.append(' '.join(c))
                return 
            for j in range(i+1,len(s)+1):
                if s[i:j] in h:
                    c.append(s[i:j])
                    dfs(j)
                    c.pop()
            return
        res=[]
        c=[]
        dfs(0)
        return res
        