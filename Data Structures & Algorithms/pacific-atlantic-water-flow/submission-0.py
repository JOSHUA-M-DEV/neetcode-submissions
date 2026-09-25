class Solution:
    def dfs(self,i,j,vis,arr,pre):
        if i<0 or j<0 or i>=len(arr) or j>=len(arr[i])or arr[i][j]<pre or (i,j) in vis:
            return
        vis.add((i,j))
        self.dfs(i+1,j,vis,arr,arr[i][j])
        self.dfs(i-1,j,vis,arr,arr[i][j])
        self.dfs(i,j-1,vis,arr,arr[i][j])
        self.dfs(i,j+1,vis,arr,arr[i][j])
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac=set()
        atl=set()
        for i in range(len(heights)):
            self.dfs(i,0,pac,heights,heights[i][0])
            self.dfs(i,len(heights[i])-1,atl,heights,heights[i][len(heights[i])-1])
        for j in range(len(heights[0])):
            self.dfs(0,j,pac,heights,heights[0][j])
            self.dfs(len(heights)-1,j,atl,heights,heights[len(heights)-1][j])
        l=[]
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if (i,j) in pac and (i,j) in atl:
                    l.append([i,j])
        return l


