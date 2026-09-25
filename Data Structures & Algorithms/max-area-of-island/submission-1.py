class Solution:
    def fun(self,i,j,arr,c1):
        if i<0 or i>=len(arr) or j<0 or j>=len(arr[i]) or arr[i][j]!=1:
            return 0
        arr[i][j]=0
        
        c1[0]+=1
        r=[0,0,1,-1]
        c=[1,-1,0,0]
        ans=1
        for z in range(4):
            nr=i+r[z]
            nc=j+c[z]
            ans+=self.fun(nr,nc,arr,c1)
        return ans
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j]==1:
                    c1=[0]
                    

                    
                    m=max(m,self.fun(i,j,grid,c1))
                    
                    
                    
        return m
        