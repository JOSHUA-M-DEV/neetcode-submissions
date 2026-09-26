class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s=set(wordList)
        q=deque()
        q.append(beginWord)
        ans=1
        while q:
            for _ in range(len(q)):
                node=q.popleft()
                if node==endWord:
                    return ans
                
                for i in range(len(node)):

                    for j in range(ord('a'),ord('z')+1):
                        if node[i]==chr(j):
                            continue
                        word=node[:i]+chr(j)+node[i+1:]
                        if word in s:

                            q.append(word)
                            s.remove(word)
                
            ans+=1
        
                        

                
            
        return 0

        
        