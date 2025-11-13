class Solution(object):
    def spiralOrder(self, matrix):
   
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        srow, scol, erow, ecol = 0, 0, m-1, n-1
        while srow <= erow and scol <= ecol:
            for j in range(scol, ecol+1):
                ans.append(matrix[srow][j])

            for i in range(srow+1, erow+1):
                ans.append(matrix[i][ecol])

            for j in range(ecol-1, scol-1, -1):
                if srow == erow:
                    break
                ans.append(matrix[erow][j])

            for i in range(erow-1, srow, -1):
                if scol == ecol:
                    break
                ans.append(matrix[i][scol])

            srow +=1 
            erow -=1
            scol +=1
            ecol -=1
        return ans