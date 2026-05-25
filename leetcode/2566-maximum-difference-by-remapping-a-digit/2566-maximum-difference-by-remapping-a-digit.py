class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_num = s
        for ch in s:
            if ch != '9':
                max_num = s.replace(ch, '9')
                break

        min_num = s.replace(s[0], '0')
        return int(max_num) - int(min_num)