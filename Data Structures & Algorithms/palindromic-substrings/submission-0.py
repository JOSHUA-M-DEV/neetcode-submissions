class Solution:
    def pal(self,i,j,s):
        c=0
        while i>=0 and j<len(s) and s[i]==s[j]:
            i-=1
            c+=1
            j+=1
        return c
   
   
    def countSubstrings(self, s: str) -> int:
        m=0
        for i in range(len(s)):
            m+=self.pal(i,i,s)+self.pal(i,i+1,s)
        return m



        