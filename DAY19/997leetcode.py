from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusties = {}
        if not trust:
            return 1
        for t in trust:
            if t[0] in trusties:
                trusties[t[0]] -= 1
            else:
                trusties[t[0]] = -1
            if t[1] in trusties:
                trusties[t[1]] += 1
            else:
                trusties[t[1]] = 1
        for person, trust_count in trusties.items():
            if trust_count == n - 1:
                return person
        return -1
