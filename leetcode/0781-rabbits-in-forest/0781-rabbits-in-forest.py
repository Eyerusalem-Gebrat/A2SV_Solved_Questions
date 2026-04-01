from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = 0
        freq = Counter(answers)
        for ans, count in freq.items():
            while count > 0:
                rabbits += ans + 1
                count -= (ans + 1)

            

        return rabbits
            
       