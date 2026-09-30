class Solution:
    def leftmin(self,arr):
        s=[]
        s.append(0)
        ans=[0]*len(arr)
        ans[0]=(-1,-1)
        for i in range(1,len(arr)):
            while s and arr[s[-1]]>=arr[i]:
                s.pop()
            if s:
                ans[i]=(arr[s[-1]],s[-1])
            else:
                ans[i]=(-1,-1)
            s.append(i)
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        l=self.leftmin(heights)
        arr1=heights[::-1]
        
        
        r=self.leftmin(arr1)
        r=r[::-1]
        
        ans=0
        for i in range(len(heights)):
            ans=max(ans,(heights[i]*(len(heights)-2-l[i][1]-r[i][1])))
        return ans
        