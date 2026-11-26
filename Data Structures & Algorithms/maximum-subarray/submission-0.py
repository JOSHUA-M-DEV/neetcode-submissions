class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=-100000
        s=-100000
        for i in nums:
            s=max(s+i,i)
            ans=max(ans,s)
        return ans
        