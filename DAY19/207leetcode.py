from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, graph: List[List[int]]) -> bool:
        def dfs(node, visited):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor, visited):
                    return False
            visited.remove(node)
            return True

        graph = defaultdict(list)
        for course, prereq in graph:
            graph[course].append(prereq)

        for course in range(numCourses):
            if not dfs(course, set()):
                return False

        return True
