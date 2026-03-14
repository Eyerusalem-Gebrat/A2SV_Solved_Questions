class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3

        total = 0
        for i in range(n):
            total += piles[2*i + 1]

        return total