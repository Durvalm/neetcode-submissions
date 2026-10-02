class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        graph = {n: [] for n in range(n)}
        for parent, ancestor in edges:
            graph[parent].append(ancestor)
            graph[ancestor].append(parent)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if dfs(neigh, node) == False:
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
