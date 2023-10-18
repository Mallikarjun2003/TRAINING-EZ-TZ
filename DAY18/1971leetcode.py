from ast import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        paths = defaultdict(list)

        for i in edges:
            paths[i[0]].append(i[1])
            paths[i[1]].append(i[0])

        if source == destination:
            return True  

        queue = [source]
        visited = {source: True}

        while queue:
            a = queue.pop(0)

            if a == destination:
                return True 

            for i in paths[a]:
                if i not in visited:
                    queue.append(i)
                    visited[i] = True

        return False  

