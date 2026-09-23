class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.h,self.k=nums,k
        heapq.heapify(self.h)
        while len(self.h)>self.k:
            heapq.heappop(self.h)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.h,val)
        if self.k<len(self.h):
            heapq.heappop(self.h)
        return self.h[0]
        

        
