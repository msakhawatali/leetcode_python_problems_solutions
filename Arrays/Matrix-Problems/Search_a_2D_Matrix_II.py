class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)   
        n = len(matrix[0])  
        col = 0
        while col <= m-1:
            if matrix[col][0] <= target:
                start = 0
                end = n-1
                while start <= end:
                    mid = start + (end - start) // 2
                    if matrix[col][mid] < target:
                        start = mid + 1
                    elif matrix[col][mid] > target:
                        end = mid - 1
                    else: 
                        return True
                col += 1
            else:
                return False