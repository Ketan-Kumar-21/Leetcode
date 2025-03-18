class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        MARKER = float('inf')
        def markRow(matrix, n, m, i):
            for j in range(m):
                if matrix[i][j] != 0 and matrix[i][j] != MARKER:
                    matrix[i][j] = MARKER
        def markCol(matrix, n, m, j):
            for i in range(n):
                if matrix[i][j] != 0 and matrix[i][j] != MARKER :
                    matrix[i][j] = MARKER
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    markRow(matrix, n, m, i)
                    markCol(matrix, n, m, j)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == MARKER:
                    matrix[i][j] = 0
        #return matrix