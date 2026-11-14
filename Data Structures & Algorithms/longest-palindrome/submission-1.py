class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        a: 1, b: 1, c: 4, d: 2

        every even count letter is accepted and counted towards the counter
        then only 1 odd would be accepted after, be it a 3 or 1 countt or wtv
        """
        counter = Counter(s)
        res = 0
        has_odd = False

        for char, cnt in counter.items():
            if cnt % 2 == 0:
                res += cnt
            else:
                res += cnt - 1
                has_odd = True

        if has_odd:
            res += 1

        return res


