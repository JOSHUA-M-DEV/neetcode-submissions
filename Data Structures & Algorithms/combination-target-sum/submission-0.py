class Solution:
    def fun(self,i,nums,t,l,ans):
        if i==len(nums):
            if t==0:
                ans.append(l.copy())
            return 
        if nums[i]<=t:
            l.append(nums[i])
            self.fun(i,nums,t-nums[i],l,ans)
            l.pop()
        self.fun(i+1,nums,t,l,ans)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        self.fun(0,nums,target,[],ans)
        return ans
        