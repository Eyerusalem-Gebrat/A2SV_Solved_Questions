class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target: return True
        
        n = len(mat)
        for i in range(3):
            for r in range(n):
                for c in range(n):
                    if c > r:
                        mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
            
            for r in range(n):
                mat[r].reverse()

            if mat == target:
                return True

        return False


            