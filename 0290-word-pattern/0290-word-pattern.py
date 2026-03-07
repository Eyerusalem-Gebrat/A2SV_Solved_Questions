class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        _map = {}
        for i in range(len(pattern)):
            if pattern[i] in _map:
                if _map[pattern[i]] != words[i]:
                    return False
            
            else:
                if words[i] in _map.values():
                    return False
                _map[pattern[i]] = words[i]

        return True