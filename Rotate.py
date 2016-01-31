class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(len(matrix), 1,-2):
            start = (n - i) / 2
            for i in range(i-1):
                matrix[start][start+i],matrix[start+i][n-start-1],matrix[n-start-1][n-start-i-1],\
                matrix[n-start-i-1][start] = matrix[n-start-i-1][start],matrix[start][start+i]\
                ,matrix[start+i][n-start-1],matrix[n-start-1][n-start-i-1]
        
            
        