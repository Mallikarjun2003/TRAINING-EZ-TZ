from collections import defaultdict
graph = [
    [0, 1, 4],
    [0, 2, 2],
    [1, 2, 5],
    [1, 3, 10],
    [2, 3, 3],
    [3, 4, 7],
]
def bellmanford(graph):
    distanes = [float('inf') for _ in range(5)]
    distanes[0] = 0
    for  i in graph:
        st,end,wt = i
        distanes[end]= min(distanes[st] + wt,distanes[end])
    print(distanes)
bellmanford(graph)
