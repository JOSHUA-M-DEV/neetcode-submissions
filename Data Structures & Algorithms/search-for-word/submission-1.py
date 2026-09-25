class Solution:
    def fun(self,i,j,z,arr,word):
        if z>=len(word):
            return True
        if i<0 or i>=len(arr) or j<0 or j>=len(arr[i]) or arr[i][j]!=word[z]:
            return False
        
        a=arr[i][j]
        print(a)
        arr[i][j]='.'
        
            
        


        r=[-1,1,0,0]
        c=[0,0,1,-1]
        for k in range(4):
            nr=i+r[k]
            nc=j+c[k]
            if self.fun(nr,nc,z+1,arr,word):
                return True
        arr[i][j]=a
        return False
                





    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==word[0]:
                    if self.fun(i,j,0,board,word):
                        return True
        return False


        