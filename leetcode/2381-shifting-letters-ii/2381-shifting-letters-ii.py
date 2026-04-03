from collections import defaultdict
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        for start, end, dirc in shifts:
            if dirc == 1:
                prefix[end + 1] += 1
                prefix[start] -= 1
            else:
                prefix[end + 1] -= 1
                prefix[start] += 1

        chars = []
        for c in s:
            chars.append(ord(c) - ord('a'))
        
        diff = 0
        for i in reversed(range(len(prefix))):
            diff += prefix[i]
            chars[i-1] = (chars[i-1] + diff + 26) % 26

        for i in range(len(chars)):
            chars[i] = chr(ord('a') + chars[i])

        return "".join(chars)      