class Solution:

    def encode(self, strs):
        s = ""
        steps = []
        for l in strs:
            s += l
            steps.append(len(l))
        if not strs:
            s = strs
        return s, steps

    def decode(self, encoded):
        s, steps = encoded
        if s == "":
            return [""]
        start = 0
        count = 0
        res = []

        for i, letter in enumerate(s):
            if i < start:
                continue
            new_s = s[start:steps[count] + start]
            res.append(new_s)
            start = steps[count] + start
            count += 1
        
        return res
            

