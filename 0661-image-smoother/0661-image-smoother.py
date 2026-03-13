class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        smooth = [[0 for i in range(len(img[0]))] for j in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[i])):
                _sum = 0
                count = 0
                for row in range(max(0,i-1), min(len(img), i+2)):
                    for col in range(max(0,j-1), min(len(img[i]), j+2)):
                        _sum += img[row][col]
                        count += 1
                smooth[i][j] = _sum // count

        return smooth