class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
            d[t[i]]=d.get(t[i],0)-1
        for i,j in d.items():
            if j!=0:
                
                return False
        return True
        