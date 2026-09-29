class Solution:
   
        


    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1=list(s1)
        d1=[0]*26
        d2=[0]*26
        for i in range(len(s1)):
            d1[ord(s1[i])-ord('a')]+=(ord(s1[i])-ord('a'))
            d2[ord(s2[i])-ord('a')]+=(ord(s2[i])-ord('a'))
        if d1==d2:
            return True
        for j in range(len(s1),len(s2)):
            d2[ord(s2[j])-ord('a')]+=(ord(s2[j])-ord('a'))
            if j>=len(s1):
                d2[ord(s2[j-len(s1)])-ord('a')]-=(ord(s2[j-len(s1)])-ord('a'))
           
            if d1==d2:
                print(d1,d2)
                return True
        
        return False
        