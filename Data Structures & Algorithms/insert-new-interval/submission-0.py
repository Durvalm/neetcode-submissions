class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1. detect if we'll just add the new interval or merge.

        if merge (if idx1 and idx2 within 2 other intervals):
            we need to check where the first index of new interval is and where the last index is, then merge everything in the middle
        """

        res = []

        for start, end in intervals:

            # Case 1: Current interval is BEFORE newInterval
            if end < newInterval[0]:
                res.append([start, end])

            # Case 2: Current interval is AFTER newInterval
            elif start > newInterval[1]:
                res.append(newInterval)
                newInterval = [start, end]

            # Case 3: They overlap, so MERGE
            else:
                newInterval = [
                    min(start, newInterval[0]),
                    max(end, newInterval[1])
                ]

        res.append(newInterval)
        return res
