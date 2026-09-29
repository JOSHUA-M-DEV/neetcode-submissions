class Solution:
    def pre(self,c):
        if c=='^':
            return 4
        if c=='*' or c=='/':
            return 3
        if c=='+' or c=='-':
            return 2
        return 0
         
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i.isdigit():
                s.append(int(i))
            elif i[0]=='-' and i[1:].isdigit():
                s.append(int(i))
            else:
                
                r=s.pop()
                l=s.pop()
                if i=='+':
                    s.append(l+r)
                if i=='-':
                    s.append(l-r)
                if i=='*':
                    s.append(l*r)
                if i=='/':
                    s.append(int(float(l)/r))

           
                
        

        return s[0]

        