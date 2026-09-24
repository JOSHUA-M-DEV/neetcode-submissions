class Solution:
    def pal(self,i,j,s):
        while i>=0 and j<len(s) and s[i]==s[j]:  
            i-=1
            j+=1
        return j-i-1
    

        
    def longestPalindrome(self, s: str) -> str:
        start=0
        end=0
        for i in range(0,len(s)):

            e=self.pal(i,i,s)
            o=self.pal(i,i+1,s)
            m=max(e,o)
            if m>(end-start+1):
                start=i-(m-1)//2
                end=i+(m)//2
                
        return s[start:end+1]


            



        
        