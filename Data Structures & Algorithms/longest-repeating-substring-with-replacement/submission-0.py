class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=collections.defaultdict(int)
        j=0
        mmf=0
        ans=0
        for i in range(len(s)):
            d[s[i]]+=1
            mmf=max(mmf,d[s[i]])
            while (i-j+1-mmf)>k:
                d[s[j]]-=1
                j+=1
            ans=max(ans,i-j+1)
        return ans
            
            
            


        return 0
            

        