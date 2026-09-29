class MinStack:

    def __init__(self):
        self.arr=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.minstack:
            val=min(val,self.minstack[-1])
        self.minstack.append(val)
        

    def pop(self) -> None:
        self.minstack.pop()
        return self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]

        

    def getMin(self) -> int:
        return self.minstack[-1]
        
