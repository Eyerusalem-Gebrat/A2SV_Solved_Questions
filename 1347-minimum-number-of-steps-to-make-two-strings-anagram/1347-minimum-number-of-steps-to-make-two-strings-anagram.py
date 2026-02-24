from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = Counter(s)
        t_freq = Counter(t)
        need = 0
        for key, val in s_freq.items():
            if key in t_freq:
                if s_freq[key] > t_freq[key]:
                    need += (s_freq[key] - t_freq[key])
            else:
                need += s_freq[key]

        return need