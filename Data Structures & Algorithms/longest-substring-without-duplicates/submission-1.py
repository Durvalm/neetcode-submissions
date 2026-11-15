class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        What we need:
        - go through every character in s
        - keep track of a set 
        - if the item is already in the set, dont move r, move l, remove s[l] from the set 

        """

        seen = set()
        l = 0
        longest = 0

        for r, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            longest = max(longest, r - l + 1)
        return longest