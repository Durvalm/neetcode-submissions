class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Whats the naive solution:
            recurse from index 0
            combine 0 with 1
            or discard 0 and retain only 1
        """

        n, res = len(s), 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        return res
        