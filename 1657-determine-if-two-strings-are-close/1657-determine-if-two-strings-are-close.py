from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        dict1 = Counter(word1)
        dict2 = Counter(word2)
        condition1 = Counter(dict1.values()) == Counter(dict2.values())
        condition2 = dict1.keys() == dict2.keys()
        return condition1 and condition2