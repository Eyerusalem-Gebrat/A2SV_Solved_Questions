class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        n = len(haystack)
        if k > n or needle not in haystack:
            return -1

        for i in range(n - k + 1):
            if haystack[i : i+k] == needle:
                return i
       
