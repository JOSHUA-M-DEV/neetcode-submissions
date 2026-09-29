class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.pre=self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.d={}
        self.size=capacity
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.pre=self.right,self.left
    
    def insert(self,node):
        p,n=self.right.pre,self.right
        p.next=node
        n.pre=node
        node.pre,node.next=p,n
    def remove(self,node):
        p,n=node.pre,node.next
        p.next,n.pre=n,p

        
        

    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            self.insert(self.d[key])
            return self.d[key].val
        return -1
    


    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        self.d[key]=Node(key,value)
        self.insert(self.d[key])
        if len(self.d)>self.size:
            lru=self.left.next
            self.remove(lru)
            del self.d[lru.key]
        
