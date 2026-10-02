class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for course, prereq in prerequisites:
            if course not in graph:
                graph[course] = []
            graph[course].append(prereq)

        visited = set()

        def dfs(course):
            # We're seeing the same course again
            # on the current DFS path -> cycle
            if course in visited:
                return False

            # Course has no prerequisites
            if course not in graph or graph[course] == []:
                return True

            visited.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)

            # We already proved this course can be completed.
            # Mark it as solved so we don't DFS it again.
            graph[course] = []

            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        

