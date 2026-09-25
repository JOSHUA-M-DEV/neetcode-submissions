class Solution:
    def fun(self,i,nums,l,s):
        s.append(l.copy())
           
        for j in range(i,len(nums)):
            
            l.append(nums[j])
            self.fun(j+1,nums,l,s)
            l.pop()

        
            

            
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s=[]
        l=[]
       
        self.fun(0,nums,l,s)
        
        return s
        