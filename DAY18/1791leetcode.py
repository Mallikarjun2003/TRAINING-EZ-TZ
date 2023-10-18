from ast import List
from collections import defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        paths =defaultdict(list)
        for i in edges:
            paths[i[0]].append(i[1])
            paths[i[1]].append(i[0])
        maxi = 0
        for i in paths:
            if i>maxi:
                maxi = i
        for i in paths:
            if len(paths[i]) == maxi -1:
                return i
            