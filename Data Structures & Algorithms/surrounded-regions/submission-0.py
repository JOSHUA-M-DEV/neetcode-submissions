class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        vis=set()
        def dfs(i,j):
            if i<0 or j<0 or i>=len(board) or j>=len(board[i]) or (i,j) in vis or board[i][j]=='X':
                return
            vis.add((i,j))
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i-1,j)

        for i in range(len(board)):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][len(board[i])-1]=='O':
                dfs(i,len(board[0])-1)
        for j in range(len(board[0])):
            if board[0][j]=='O':
                dfs(0,j)
            if board[len(board)-1][j]=='O':
                dfs(len(board)-1,j)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=='O' and (i,j) not in vis:
                    board[i][j]='X'
        



        
            

        