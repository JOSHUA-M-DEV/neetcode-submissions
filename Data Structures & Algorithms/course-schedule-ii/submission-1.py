class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(numCourses)}
        vis,cycle=set(),set()
        ans=[]
        def dfs(i):
            if i in cycle:
                return False
            if i in vis:
                return True
            cycle.add(i)
            for j in adj[i]:

                if not dfs(j):
                    return False
            cycle.remove(i)
            vis.add(i)
            ans.append(i)
            return True

            
            
        for c,p in prerequisites:
            adj[c].append(p)

        for c in range(numCourses):
            if not dfs(c):
                return []
        return ans
        
        