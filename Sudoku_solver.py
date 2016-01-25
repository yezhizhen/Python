class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #driver of starting
        #first find the place to start
        
        self.solveunit(board,0,0)
                        
                        
    def findtosolve(self, board, x, y):
        for r in range(x,9):
            for c in range(y, 9):
                if board[r][c] == '.':
                    return r,c
        for r in range(0,9):
            for c in range(0,y):
                if board[r][c] =='.':
                    return r,c
        for r in range(0,x):
            for c in range(y,9):
                if board[r][c] =='.':
                    return r,c
                        
        return -1, -1        
                
    def solveunit(self, board, x, y):
        x,y = self.findtosolve(board, x, y)
        if  x == -1:
            return True

        for val in range(1,10):
            if self.checkValidity(board, x,y, str(val)):
                board[x][y] = str(val)
                if self.solveunit(board,x,y):
                    return True
                board[x][y] = '.'
        # after you have tried all
        return False
            
        
        
        
    def checkValidity(self, board, x, y, target):
        """
        :rtype: bool
        """
        #check row
        for i in range(9):
            if target == board[x][i] and i != y:
                return False
            if target == board[i][y] and i != x:
                return False
        #check 9 square
        index_x = x//3 *3
        index_y = y//3 *3
        for _1 in range(index_x,index_x+3):
            for _2 in range(index_y,index_y+3):
                if target == board[_1][_2] and not(x==_1 and y==_2):
                    return False
        
        return True 
        