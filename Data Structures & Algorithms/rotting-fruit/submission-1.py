class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        empty=0
        cell=0
        

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    q.append([i,j])
                    cell+=1
                elif grid[i][j]==1:
                    cell+=1
                else:
                    empty+=1
        if cell==0:
            return 0
        count=0
        while q:
            
            for _ in range(len(q)):
                cell-=1
                r,c=q.popleft()
                r1=[0,0,-1,1]
                c1=[-1,1,0,0]
                for z in range(0,4):
                    nr=r+r1[z]
                    nc=c+c1[z]
                    if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[nr]) and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append([nr,nc])
            count+=1
        print(count)
        if cell==0:
            return count-1
        return -1

                    


        


                    
                

        