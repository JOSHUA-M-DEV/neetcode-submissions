class Solution:
    def fun(self,l,r,s,ans,n):
        if len(s)== 2*n:
            ans.append(s)
            return
        if l<n:
            self.fun(l+1,r,s+'(',ans,n)
        if r<l:
            self.fun(l,r+1,s+')',ans,n)


    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        self.fun(0,0,"",ans,n)
        return ans
        