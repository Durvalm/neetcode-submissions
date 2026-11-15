class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        go through points, store the euclidean distance + points
        sort by euclidean dist, return top k points
        """


        arr = []
        res = []

        for x, y in points:
            dist = (x-0)**2 + (y-0)**2
            arr.append([dist, [x, y]])
        
        arr.sort()
        for i in range(k):
            res.append(arr[i][1])
        
        return res