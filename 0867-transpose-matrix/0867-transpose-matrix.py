class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for i in range(len(matrix[0])):
            transpose.append([matrix[j][i] for j in range(len(matrix))])

        return transpose