class Solution:
    def fun(self,c,arr,ans,row,up,down,n):
        if c==n:
            ans.append(["".join(s) for s in arr])
            return
        
        for i in range(0,n):
            if row[i] and down[i+c] and up[n+(i-c)+1]:
                row[i]=False
                down[i+c]=False
                up[n+(i-c)+1]=False
                arr[i][c]='Q'
                self.fun(c+1,arr,ans,row,up,down,n)
                row[i]=True
                down[i+c]=True
                up[n+(i-c)+1]=True
                arr[i][c]='.'






    def solveNQueens(self, n: int) -> List[List[str]]:
        arr=[['.']*n for _ in range(n)]
       
        
        up=[True]*(2*n +1)
        down=[True]*(2*n +1)
        row=[True]*(n)
        ans=[]
        self.fun(0,arr,ans,row,up,down,n)

        
        return ans

        

        