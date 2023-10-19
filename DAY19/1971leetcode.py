from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        paths = defaultdict(list)
        for i in edges:
            paths[i[0]].append(i[1])
            paths[i[1]].append(i[0])
        if source == destination:
            return True  

        stack = [source]
        visited = {source: True}

        while stack:
            a = stack.pop()

            if a == destination:
                return True 
            for i in paths[a]:
                if i not in visited:
                    stack.append(i)
                    visited[i] = True
        return False  

