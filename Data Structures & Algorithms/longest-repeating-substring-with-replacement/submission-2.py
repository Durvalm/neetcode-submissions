class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        l = 0
        longest = 0

        for r in range(len(s)):
            cnt[s[r]] += 1
            # check if our window is valid
            # max item in count - length + k (thats the formula for validity)
            max_char = max(cnt.values())
         
            window_size = r - l + 1
            is_valid = (max_char - window_size + k) >= 0
            if is_valid:
                longest = max(longest, (window_size))
            else:
                cnt[s[l]] -= 1
                l += 1
        return longest



            
        