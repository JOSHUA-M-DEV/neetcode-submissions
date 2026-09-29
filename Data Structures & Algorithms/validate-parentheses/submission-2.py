class Solution:
    def isValid(self, arr: str) -> bool:
        s=[]
        for i in arr:
            print(s)
            if i in '({[':
                s.append(i)
            else:
                if not s:
                    return False
                if s[-1]=='(' and i!=')':
                    return False
                if s[-1]=='[' and i!=']':
                    return False
                if s[-1]=='{' and i!='}':
                    return False
                s.pop()
        if len(s)>0:
            return False
        return True
                
        