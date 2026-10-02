class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        """
        queue [('X', i + n + 1)]
        queue [('X', 3), ('Y', 4)]
        heap [x, count:2, y, count:2]
        i=0 process max count (X)
        add to the queue -> [('X', 3), ...]
        i=1 process max count (Y)
        add to the queue -> [('X', 3), ('Y', 4), ...]
        """
        cnt = Counter(tasks)
        maxHeap = [-cnt for cnt in cnt.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time