class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={i:[] for i in range(numCourses)}
        vis=set()
        def dfs(i):
            if i in vis:
                return False
            if adj[i]==[]:
                return True
            vis.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            vis.remove(i)
            adj[i]=[]
            return True
            
        for curr,pre in prerequisites:
            adj[curr].append(pre)
        for c in range(len(prerequisites)):
            if not dfs(prerequisites[c][0]):
                return False

        return True
        