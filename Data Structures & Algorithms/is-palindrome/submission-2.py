class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1

        while l <= r:
            lc, rc = s[l], s[r]
            if not lc.isalnum():
                l += 1
                continue
            if not rc.isalnum():
                r -= 1
                continue
            lc, rc = lc.lower(), rc.lower()
            if lc == rc:
                l += 1
                r -= 1
            else:
                return False
        return True