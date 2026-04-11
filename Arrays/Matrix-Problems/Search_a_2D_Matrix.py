class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m*n-1

        while start <= end:
            mid = start + (end-start)//2
            row = mid//n
            
            col = int(mid%n)
            print(col)
            if matrix[row][col] > target:
                end = mid - 1
            elif matrix[row][col] < target:
                start = mid + 1
            else:
                return True
        return False
            