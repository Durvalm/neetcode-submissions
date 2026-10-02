class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        res = None
        for n in nums:
            heapq.heappush(heap, -n)
        
        heapq.heapify(heap)

        for _ in range(k):
            res = heapq.heappop(heap)
        return -(res)
