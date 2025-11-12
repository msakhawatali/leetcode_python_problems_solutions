import numpy as np
class Solution(object):
    def searchMatrix(self, mat, target):

        matrix = np.array(mat)
        rows, cols = matrix.shape
        r, c = 0, cols-1
        while r < rows and c >= 0:
            if target == mat[r][c]:
                return True
            elif target < mat[r][c]:
                c -= 1
            else:
                r += 1
        return False
