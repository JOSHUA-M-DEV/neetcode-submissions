class Solution:
    # def pal(self,i,j,s):
    #     c=0
    #     while i>=0 and j<len(s) and s[i]==s[j]:
    #         i-=1
    #         c+=1
    #         j+=1
    #     return c
   
   
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
        return res



        