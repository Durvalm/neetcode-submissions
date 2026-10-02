class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                popped = stack.pop()
                dist = i - popped[1]
                res[popped[1]] = dist
            
            stack.append((temp, i))
        return res