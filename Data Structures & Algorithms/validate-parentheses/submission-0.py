class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for char in s:
            stack.append(char)
            is_closing = char in map
            if is_closing and len(stack) > 1:
                if map[char] == stack[-2]:
                    stack.pop()
                    stack.pop()
        if len(stack) > 0:
            return False
        return True