class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l=0
        ans=0
        for i in range(len(s)):
            while s[i] in d:
                del d[s[l]]
                l+=1
            d[s[i]]=1
            ans=max(ans,i-l+1)
        return ans 
            
            

        