class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(len(edges)+1)}
        def dfs(i,target):
            vis=[False]*(len(edges)+1)
            q=[i]
            while q:
                val=q.pop()
                if val==target:
                    return True
                
                for j in adj[val]:
                    if not vis[j]:
                        vis[j]=True
                        q.append(j)
            return False



                

        for c,p in edges:
            if dfs(c,p):
                return [c,p]
            adj[c].append(p)
            adj[p].append(c)

            
        return [0,0]
        