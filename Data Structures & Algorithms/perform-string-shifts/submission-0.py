class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        """
    Input: s = "abc", shift = [[0,1],[1,2]]

    Output: "cab"

    create new string?
    if 0 we slice it base = s[0:shift[i][1]]  ;  rest = [shift[i][1] : len(s)]
    if 1 we lice it base = s[-1: negative(shift[i][1]) ]  ;  rest = negative(shift[i][1]) : 0

    new string = rest + base
    
        """

        prev_s = s

        for direction, amount in shift:
            new_s = ""

            if direction == 0:
                base = prev_s[0:amount]
                rest = prev_s[amount:len(s)]
                new_s = rest + base

            elif direction == 1:
                base = prev_s[len(s) -amount:]
                rest = prev_s[:len(s) -amount]
                new_s = base + rest

            prev_s = new_s
        return prev_s