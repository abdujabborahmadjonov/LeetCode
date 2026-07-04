from collections import defaultdict
from typing import List

s = 4
roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
graph = defaultdict(list)
def minScore(n: int, roads: List[List[int]]) -> int:


       for l,r,w in roads:
           graph[l].append((r,w))
           graph[r].append((l,w))
       print(graph)
       visited = set()

       ans = float("inf")

       def dfs(node):
           nonlocal ans
           visited.add(node)

           for nei, w in graph[node]:
               ans = min(ans, w)
               if nei not in visited:
                   dfs(nei)
       dfs(1)
       return ans


print(minScore(s, roads))
