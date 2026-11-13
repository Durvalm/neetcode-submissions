class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for c in ransomNote:
            counter[c] -= 1
            if counter[c] < 0:
                return False
        return True