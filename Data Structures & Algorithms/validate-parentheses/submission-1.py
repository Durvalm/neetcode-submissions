class Solution:
    def isValid(self, s: str) -> bool:
        """

        """
        _map = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []

        for c in s:
            stack.append(c)
            
            if c in _map:
                if len(stack) > 1 and stack[-2] == _map[stack[-1]]:
                    stack.pop()
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False

