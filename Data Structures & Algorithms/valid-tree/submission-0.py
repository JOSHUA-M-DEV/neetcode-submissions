class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj={i:[] for i in range(n)}
        for c,p in edges:
            adj[c].append(p)
            adj[p].append(c)
        vis=set()
        def dfs(i,p):
            
            if i in vis:
                return False
            
            vis.add(i)
            for j in adj[i]:
                if j==p:
                    continue
                if not dfs(j,i):
                    return False

            
            
            return True
            
        
      
        return dfs(0,-1) and len(vis)==n


            
        