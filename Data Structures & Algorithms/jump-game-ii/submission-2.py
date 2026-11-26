class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0

        ans=0
        c=0
        j=0
        for i in range(len(nums)):
            ans=max(ans,i+nums[i])
            if i==c:
                c=ans
                j+=1
                if c>=len(nums)-1:
                    break
        return j


            
        