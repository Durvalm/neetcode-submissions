class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {k: [] for k in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()
        
        def dfs(crs):
            if crs in visiting:
                return False
            if graph[crs] == []:
                return True
            
            visiting.add(crs)
            for prereq in graph[crs]:
                if not dfs(prereq):
                    return False
            visiting.remove(crs)
            graph[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


