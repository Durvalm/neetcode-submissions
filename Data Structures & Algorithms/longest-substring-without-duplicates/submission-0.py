class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0

        l = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            longest = max(longest, r - l + 1)

        return longest

        # 3 - (z x y) x
        #  - (z [x] y x)