class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m=0
        for i in range(len(nums)):
            if m<i:
                return False
            m=max(m,nums[i]+i)
            if m>=len(nums):
                return True
        return True
            
        