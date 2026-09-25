class Solution:
    def fun(self,i,s,d,ans,res):
        if i==len(s):
            if ans!="":
                res.append(ans)
            return
        val=d[s[i]]
        for j in range(0,len(val)):
            self.fun(i+1,s,d,ans+val[j],res)
        


    def letterCombinations(self, digits: str) -> List[str]:
        d={}
        d["2"]="abc"
        d["3"]="def"
        d["4"]="ghi"
        d["5"]="jkl"
        d["6"]="mno"
        d["7"]="pqrs"
        d["8"]="tuv"
        d["9"]="wxyz"
        res=[]
        self.fun(0,digits,d,"",res)
        return res
        