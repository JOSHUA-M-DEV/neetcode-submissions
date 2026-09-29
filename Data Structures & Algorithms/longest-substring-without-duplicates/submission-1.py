class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        j=0
        m=0
        for i in range(len(s)):
            
            while s[i] in d:
                del d[s[j]]
                j+=1
            d[s[i]]=i
            m=max(m,i-j+1)
        return m
            

        