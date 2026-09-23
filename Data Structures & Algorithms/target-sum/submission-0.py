class Solution:
    def fun(self,i,arr,k,dp):
        if len(arr)==i:
            if k==0:
                return 1
            return 0
        
        if (i,k) in dp:
            return dp[(i,k)]
        
        
            
        dp[(i,k)]=self.fun(i+1,arr,k-arr[i],dp)+self.fun(i+1,arr,k+arr[i],dp)
        return dp[(i,k)]
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        return self.fun(0,nums,target,dp)


        