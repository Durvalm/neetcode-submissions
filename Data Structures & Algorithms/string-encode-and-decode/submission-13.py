class Solution:

    def encode(self, strs):
        new_str = ""
        for s in strs:
            new_str += str(len(s)) + "#" + s
        return new_str

    def decode(self, encoded):
        res = []
        i = 0

        while i < len(encoded):
            j = i
            while encoded[j] != "#":
                j += 1
            length = int(encoded[i:j])
            res.append(encoded[j + 1 : length + j + 1])
            i = length + j + 1
        
        return res
           

            

     

