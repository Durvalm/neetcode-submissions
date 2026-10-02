class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hashmap:
            return ""
        
        max_timestamp = float('-inf')
        res = ""
        timestamps = self.hashmap[key]
        l = 0
        r = len(timestamps) - 1

        while l <= r:
            mid = (l + r) // 2
            if timestamp == timestamps[mid][0]:
                return timestamps[mid][1]
            elif timestamp < timestamps[mid][0]:
                r = mid - 1
            else:
                max_timestamp = timestamps[mid][0]
                res = timestamps[mid][1]
                l = mid + 1
        return res

        
