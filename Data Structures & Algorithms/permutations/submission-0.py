class Solution:
    def fun(self,i,nums,ans):
        if i==len(nums):
            ans.append(nums.copy())
            return
        for j in range(i,len(nums)):
            nums[i],nums[j]=nums[j],nums[i]
            self.fun(i+1,nums,ans)
            nums[i],nums[j]=nums[j],nums[i]
            

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.fun(0,nums,ans)
        return ans
        