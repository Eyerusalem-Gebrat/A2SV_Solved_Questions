class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.add(j)

        for row in rows:
            for j in range(len(matrix[row])):
                matrix[row][j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j in cols:
                    matrix[i][j] = 0