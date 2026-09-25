class Solution:
    def fun(self,i,j,q,vis,arr):
        if i<0 or j<0 or i>=len(arr) or j>=len(arr[i]) or ((i,j) in vis) or arr[i][j]==-1:

            return
        vis.add((i,j))
        q.append([i,j])
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        vis=set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==0:
                    q.append([i,j])
                    vis.add((i,j))
        dis=0
        while q:

            for _ in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dis
                self.fun(r+1,c,q,vis,grid)
                self.fun(r-1,c,q,vis,grid)
                self.fun(r,c+1,q,vis,grid)
                self.fun(r,c-1,q,vis,grid)

            dis+=1






        