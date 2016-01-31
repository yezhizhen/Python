from Sudoku_solver import Solution

obj = Solution()

raw_input("You can modify the board in the board.dat. Press Enter to continue.\n")

board = []
with open('board.dat', 'r') as f:
	f.readline()
	for line in f:
		line = line.strip('\n')
		temp = []
		for char in line:
			temp.append(char)
		board.append(temp)
if obj.solveSudoku(board):
	print "Problem solved. We are now printing"
else:
	print "No solution found! You SB!"

for line in board:
	print(line)
raw_input("Program Finished. Enter to exit.\n T_T")