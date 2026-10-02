
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = Counter(s1)
        window = Counter()

        l = 0

        for r in range(len(s2)):
            # Add new character to window
            window[s2[r]] += 1

            # If window becomes too big, remove leftmost character
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1

            # Check whether this window is a permutation
            if window == target:
                return True

        return False
 