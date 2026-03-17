class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)
        h = 0
        for i in range(n):
            if citations[i] >= i + 1:
                h = max(h, i + 1)

        return h