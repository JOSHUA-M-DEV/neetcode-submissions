class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=-10000
        mi=1000
        for i in prices:
            mi=min(mi,i)
            m=max(m,i-mi)
        return m
        