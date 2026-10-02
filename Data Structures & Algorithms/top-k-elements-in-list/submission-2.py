class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        hashmap = {}

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 0
            hashmap[n] += 1

        for n, freq in hashmap.items():
            heapq.heappush(heap, (-freq, n))

        # Step 3: take k most frequent
        for _ in range(k):
            freq, n = heapq.heappop(heap)
            res.append(n)

        return res
