class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        res = []
        
        left, right, top, bottom = 0, col - 1, 0, row - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                cur = matrix[top][i]
                res.append(cur)

            top += 1

            for i in range(top, bottom + 1):
                cur = matrix[i][right]
                res.append(cur)
            
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    cur = matrix[bottom][i]
                    res.append(cur)

                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):            
                    cur = matrix[i][left]
                    res.append(cur)

                left += 1
            
        return res