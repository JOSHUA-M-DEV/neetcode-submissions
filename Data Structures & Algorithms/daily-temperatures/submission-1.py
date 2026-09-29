class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        s=[]
        s.append((temperatures[n-1],n-1))

        ans=[0]*n
        for i in range(n-2,-1,-1):
            while len(s)>0 and s[-1][0]<=temperatures[i]:

                s.pop()
            if s:
                ans[i]=s[-1][1]-i
            else:
                ans[i]=0

            s.append((temperatures[i],i))
        return ans


            
    
            

        
        

            

            


            


        