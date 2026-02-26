class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        j = 0
        unique = set()
        for i in range(len(s)):
            while s[i] in unique:
                unique.remove(s[j])
                j += 1
            unique.add(s[i])
            longest = max(longest, i - j + 1)
        return longest



                