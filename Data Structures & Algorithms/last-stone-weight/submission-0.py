class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # get the 2 heaviest stones (they're in negative form)
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            delta = abs(x) - abs(y)
            if delta > 0:
                heapq.heappush(heap, -delta)
        if len(heap) > 0:
            return abs(heap[-1])
        return 0