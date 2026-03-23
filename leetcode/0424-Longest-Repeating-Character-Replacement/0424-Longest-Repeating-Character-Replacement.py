from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        chars = defaultdict(int)
        longest = 0

        while r < len(s):
            chars[s[r]] += 1
            size = r - l + 1
            if size - max(chars.values()) <= k:
                r += 1
            else:
                while size - max(chars.values()) > k:
                    chars[s[l]] -= 1
                    l += 1 
                    size = r - l + 1  
                r += 1        
            
            longest = max(longest, r - l)

            
        return longest