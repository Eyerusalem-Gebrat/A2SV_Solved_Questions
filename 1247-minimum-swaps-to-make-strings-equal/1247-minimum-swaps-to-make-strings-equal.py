class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        i = 0
        xy_mis = 0
        yx_mis = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    xy_mis += 1
                else:
                    yx_mis += 1
            i += 1
            
        swap = (xy_mis // 2) + (yx_mis // 2)
        if xy_mis % 2 == 1 and yx_mis % 2 == 1:
            return swap + 2
        elif xy_mis % 2 == 0 and yx_mis % 2 == 0:
            return swap
        else:
            return -1

