class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1
        return s[resIdx : resIdx + resLen]

        # res = ""
        # visited = set()

        # def dfs(i, j):
        #     nonlocal res
        #     if ((j - i) < 1 or
        #          i < 0 or j > len(s) or i >= j
        #          or (i, j) in visited):
        #         return
            
        #     visited.add((i, j))

        #     if s[i:j] == s[i:j][::-1]:
        #         if (j - i) > len(res):
        #             res = s[i:j]

        #     dfs(i + 1, j)
        #     dfs(i, j + 1)

        # dfs(0, 1)
        # return res
