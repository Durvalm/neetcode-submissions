class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {node: [] for node in range(n)}

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visit = set()
        occurences = 0

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for neigh in graph[node]:
                dfs(neigh)



        for node in graph:
            if node not in visit:
                dfs(node)
                occurences += 1
        return occurences 