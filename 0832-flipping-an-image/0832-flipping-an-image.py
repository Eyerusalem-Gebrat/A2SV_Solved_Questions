class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for r in range(n):
            image[r].reverse()
        
        for r in range(n):
            for c in range(n):
                if image[r][c] == 0:
                    image[r][c] = 1
                else: 
                    image[r][c] = 0

        return image