class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = {node: [] for node in range(n + 1)}

        def dfs(node, parent):
            if node in visit:
                return True
            
            visit.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    return True
            return False

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            visit = set()
            if dfs(u, -1):
                return [u, v]
        return []