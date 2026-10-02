class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for course, prereq in prerequisites:
            if course not in graph:
                graph[course] = []

            graph[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if not graph.get(course):
                return True

            visiting.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)

            # We've proven this course has no cycle downstream
            graph[course] = []

            return True

        for course in graph:
            if not dfs(course):
                return False

        return True