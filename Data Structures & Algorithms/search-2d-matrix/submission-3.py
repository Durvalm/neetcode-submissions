class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                # it's here
                return self.check_row(matrix[mid], target)

            elif target >= matrix[mid][0] and target >= matrix[mid][-1]:
                start = mid + 1
            elif target <= matrix[mid][0]:
                end = mid - 1
        return False

    def check_row(self, row, target):
        l = 0
        r = len(row) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > row[mid]:
                l = mid + 1
            elif target < row[mid]:
                r = mid - 1
            else:
                return True
        return False

