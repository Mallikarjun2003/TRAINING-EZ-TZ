class Solution:
    def allPathsSourceTarget(self, graph):
        result = []
        def dfs(node, path):
            if node == len(graph)-1:
                result.append(path)
                return
            for i in graph[node]:
                dfs(i, path + [i])
        dfs(0, [0]) 
        return result
