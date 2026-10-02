class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter()
        target = Counter(t)
        l = 0
        best_l = 0
        best_r = 0
        best_length = float("inf")

        for r in range(len(s)):
            cnt[s[r]] += 1
            # While current window contains everything we need
            while self.has_substring(cnt, target):

                # Current window is valid.
                # Check whether it's the smallest we've seen.
                if r - l + 1 < best_length:
                    best_length = r - l + 1
                    best_l = l
                    best_r = r

                char = s[l]
                cnt[char] -= 1

                if cnt[char] == 0:
                    del cnt[char]

                l += 1

        if best_length == float("inf"):
            return ""

        return s[best_l:best_r + 1]

    def has_substring(self, cnt, target):
        for letter, count in target.items():
            if cnt[letter] < count:
                return False

        return True
