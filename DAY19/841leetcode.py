from ast import List
from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        paths = defaultdict(list)
        for key,room in enumerate(rooms):
            paths[key].extend(room)
        stack =[0]
        while(stack):
            a = stack.pop()
            visited.add(a)
            for i in paths[a]:
                if i not in visited:
                    stack.append(i)
        return len(visited) == len(rooms)

