class Solution:
    def pal(self,i,j,s):
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

    def fun(self,i,s,l,ans):
        if i==len(s):
            ans.append(l.copy())
            return 
        for j in range(i,len(s)):

            
            if self.pal(i,j,s):

                l.append(s[i:j+1])
                self.fun(j+1,s,l,ans)
                l.pop()

    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        self.fun(0,s,[],ans)
        return ans
        