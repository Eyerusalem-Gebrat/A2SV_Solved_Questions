class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""

        for o in order:
            for c in s:
                if c == o:
                    res += c

        for c in s:
            if c not in order:
                res += c

        return res