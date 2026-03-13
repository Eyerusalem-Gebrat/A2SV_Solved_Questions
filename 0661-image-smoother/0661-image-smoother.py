class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        smooth = [[0 for i in range(len(img[0]))] for j in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[i])):
                _sum = 0
                count = 0
                for row in range(i-1, i+2):
                    for col in range(j-1, j+2):
                        if 0 <= row < len(img) and 0 <= col < len(img[i]):
                            _sum += img[row][col]
                            count += 1
                smooth[i][j] = _sum // count

        return smooth