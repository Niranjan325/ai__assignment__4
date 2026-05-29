board = [
[3,0,6,5,0,8,4,0,0],
[5,2,0,0,0,0,0,0,0],
[0,8,7,0,0,0,0,3,1],
[0,0,3,0,1,0,0,8,0],
[9,0,0,8,6,3,0,0,5],
[0,5,0,0,9,0,6,0,0],
[1,3,0,0,0,0,2,5,0],
[0,0,0,0,0,0,0,7,4],
[0,0,5,2,0,6,3,0,0]
]

def valid(board,row,col,num):

    for x in range(9):
        if board[row][x]==num:
            return False

    for x in range(9):
        if board[x][col]==num:
            return False

    startRow=row-row%3
    startCol=col-col%3

    for i in range(3):
        for j in range(3):
            if board[startRow+i][startCol+j]==num:
                return False

    return True

def solve(board):

    for row in range(9):
        for col in range(9):

            if board[row][col]==0:

                for num in range(1,10):

                    if valid(board,row,col,num):

                        board[row][col]=num

                        if solve(board):
                            return True

                        board[row][col]=0

                return False

    return True

solve(board)

for row in board:
    print(row)
