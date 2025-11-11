import numpy as np
class Solution(object):
    def searchMatrix(self, matrix, target):

        def SearchInRow(matrix, target, midRow):
            matrix_np = np.array(matrix)
            rows, cols = matrix_np.shape
            st, end = 0, cols - 1
            while st <= end:
                mid = st + ((end - st)/2)
                if target == matrix[midRow][mid]:
                    return True
                elif target > matrix[midRow][mid]:
                    st = mid + 1
                else:
                    end = mid - 1
            return False

        matrix_np = np.array(matrix)
        rows, cols = matrix_np.shape
        startRow, endRow = 0, rows - 1
        while startRow <= endRow:
            midRow = startRow + ((endRow - startRow)/2)
            if target >= matrix[midRow][0] and target <= matrix[midRow][cols - 1]:
                return SearchInRow(matrix, target, midRow)
            elif target >= matrix[midRow][cols - 1]:
                startRow = midRow + 1
            else : 
                endRow = midRow - 1
        return False
        