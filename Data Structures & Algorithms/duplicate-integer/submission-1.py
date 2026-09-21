class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=set()
        for i in nums:
            if i in l:
                return True
            l.add(i)
        return False
        