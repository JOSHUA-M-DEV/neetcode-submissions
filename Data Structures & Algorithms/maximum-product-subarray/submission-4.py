class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=1
        r=1
        m=nums[0]
        for i in range(len(nums)):
            l*=nums[i]
            r*=nums[len(nums)-i-1]
           
            m=max(m,max(l,r))
            if l==0:
                l=1
            if r==0:
                r=1
        return m

        