class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = r

        while l <= r:
            k = (l + r) // 2

            total_time = 0
            for p in piles:
                k_needed_to_finish = math.ceil(float(p) / k)
                total_time += k_needed_to_finish

            if total_time <= h:
                min_k = k
                r = k - 1
            else:
                l = k + 1
        return min_k


