class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for s in strs:
            _map = [0] * 26
            for letter in s:
                _map[ord(letter) - ord('a')] += 1
            if tuple(_map) not in hashmap:
                hashmap[tuple(_map)] = []
            hashmap[tuple(_map)].append(s)
        return list(hashmap.values())
            
        