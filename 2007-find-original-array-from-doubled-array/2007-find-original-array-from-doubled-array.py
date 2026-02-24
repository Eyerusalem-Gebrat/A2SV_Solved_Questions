from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0: return []
        original = []
        changed.sort()
        _dict = Counter(changed)
        if 0 in _dict:
            k = _dict[0]
            if k % 2 != 0: return []
            else: 
                original.extend([0] * (k // 2))
                _dict.pop(0)
        
        for key, val in _dict.items():
            if _dict[key] == 0: continue
            
            while _dict[key] > 0:
                if (key * 2) not in _dict or _dict[key*2] == 0:
                    return []
                original.append(key)
                _dict[key] -= 1
                _dict[key*2] -= 1
        

        return original
