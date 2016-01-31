class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        #has 2n-1 diagnoals in one side
        #True means free
        
        if n == 1:
            return [['Q']]
        if n == 2 or n == 3:
            return []
        col = [True for i in range(n)]
        rd = [True for i in range(2*n-1)]
        ld = [True for i in range(2*n-1)]
        ans = []
        tempans =[['.' for i in range(n)] for i in range(n)] 
        def backtrace(row):
            if row >= n:
                c = []
                for r in tempans:
                    c.append(''.join(r))
                ans.append(c)
                #notify that end reached
                return 
            for c in range(n):
                #if this is safe
                if col[c] and rd[row+c] and ld[row-c+n-1]:
                    tempans[row][c] = 'Q'
                    col[c] = False
                    rd[row+c] = False
                    ld[row-c+n-1] = False
                    #finished
                    backtrace(row+1)
                    tempans[row][c] = '.'
                    col[c] = True
                    rd[row+c] = True
                    ld[row-c+n-1] = True
        #Let's go through every row. Since every row has exactly one element
        backtrace(0)
        return ans
