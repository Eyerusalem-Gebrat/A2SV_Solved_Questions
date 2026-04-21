class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = 0
        col = 0
        diagonal = []
        flag = True
        
        while 0 <= row < len(mat) and 0 <= col < len(mat[0]):
            if flag:
                while 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                    diagonal.append(mat[row][col])
                    row -= 1
                    col += 1
                row += 1
                if col == len(mat[0]):
                    row += 1
                    col -= 1
                flag = False
                
                

            else:
                while 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                    diagonal.append(mat[row][col])
                    row += 1
                    col -= 1
                col += 1
                if row == len(mat):
                    col += 1
                    row -= 1
                flag = True
                

        return diagonal

