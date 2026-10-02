class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt_res = Counter(s1)

        l = 0
        cur_cnt = Counter()
        for r in range(len(s2)):
            len_equivalent = sum(cur_cnt.values()) == sum(cnt_res.values())
            if len_equivalent and cur_cnt != cnt_res:
                l += 1
            cur_cnt = Counter(s2[l:r+1])
            print(cur_cnt)
            if cur_cnt == cnt_res:
                return True
        return False

 