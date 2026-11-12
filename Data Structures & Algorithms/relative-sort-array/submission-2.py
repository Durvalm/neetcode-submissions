class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        first approach: 3 passes
        1- make counter
        2- go through arr2, and add items * count to new array
        3- go through arr1 and add remaining items in order to new array 

        time complexity arr1*arr1*arr2


        approach 2:
            go through arr1 in a while loop, maintain a pointer in arr2 
            keep iterating through arr1 in an exponential manner.

            complexity arr1^2
        """

        # res = []

        # for num2 in arr2:
        #     for i, num1 in enumerate(arr1):
        #         if num2 == num1:
        #             res.append(num1)
        #             arr1[i] = -1
        # arr1.sort()

        # for num1 in arr1:
        #     if num1 != -1:
        #         res.append(num1)
        # return res

        count = Counter(arr1)
        res = []

        for num2 in arr2:
            res += [num2] * count[num2]
            del count[num2]
        
        for num in sorted(count):
            res += [num] * count[num]
        
        return res

