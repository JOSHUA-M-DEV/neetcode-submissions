class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        d=deque([])
        ans=[]
        for i in range(len(nums)):
            if d and d[0]<=(i-k):
                d.popleft()
            while d and nums[d[-1]]<nums[i]:
                d.pop()
            d.append(i)
            if i>=k-1:
                ans.append(nums[d[0]])
            
            
        return ans


            
            
        