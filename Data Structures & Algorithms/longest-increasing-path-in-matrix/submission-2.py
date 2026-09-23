class Solution:
    def fun(self,i,j,arr,dp):
        if i>=len(arr) or j>=len(arr[i]) or i<0 or j<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]

        r=[-1,1,0,0]
        c=[0,0,1,-1]
        dp[i][j]=1
        for z in range(0,4):
            nr=r[z]+i
            nc=c[z]+j
            if nr>=0 and nr<len(arr) and nc>=0 and nc<len(arr[nr]) and arr[nr][nc]>arr[i][j]:
                dp[i][j]=max(1+self.fun(nr,nc,arr,dp),dp[i][j])
        return dp[i][j]




    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp=[[-1]*(len(matrix[0])+1) for _ in range(len(matrix))]

        res=0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]>=0:
                    res=max(res,self.fun(i,j,matrix,dp))
           
        return res


        