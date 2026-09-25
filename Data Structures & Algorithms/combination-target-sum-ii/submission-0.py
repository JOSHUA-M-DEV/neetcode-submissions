class Solution:
    def fun(self,i,nums,t,l,ans):
        if t==0:
            ans.append(l.copy())
            return
        if i==len(nums):
            print(l)
            if t==0:
                
                ans.append(l.copy())
            return 
        for j in range(i,len(nums)):
            if j>i and nums[j]==nums[j-1]:
                continue
            
            if nums[j]>t:
                break
            print(nums[j])
            l.append(nums[j])
            self.fun(j+1,nums,t-nums[j],l,ans)
            l.pop()
            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        self.fun(0,candidates,target,[],ans)
        return ans
        