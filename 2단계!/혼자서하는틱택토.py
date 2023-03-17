'''
1. "O"의 개수 >= "X"의 개수
2. "O"에 한 줄이 완성되면 "O"의 개수 = "X"의 개수 + 1
3. "X"에 한 줄이 완성되면 "O"의 개수 = "X"의 개수
4. 둘 다 안될 때 => "O"가 "X"보다는 많거나 같으면 된다.
'''
def solution(board):
    def finished(i,j):
        nonlocal board
        # 가로를 먼저 확인한다.
        if board[i][0] == board[i][1] == board[i][2]:
            return True
        # 세로를 확인한다.
        elif board[0][j] == board[1][j] == board[2][j]:
            return True
        # 대각선을 확인한다.
        elif i == 0 and j == 0 and board[0][0] == board[1][1] == board[2][2]:
            return True
        elif i == 2 and j == 2 and board[0][0] == board[1][1] == board[2][2]:
            return True
        elif i == 1 and j == 1 and board[0][0] == board[1][1] == board[2][2]:
            return True
        elif i == 1 and j == 1 and board[0][2] == board[1][1] == board[2][0]:
            return True
        elif i == 0 and j == 2 and board[0][2] == board[1][1] == board[2][0]:
            return True
        elif i == 2 and j == 0 and board[0][2] == board[1][1] == board[2][0]:
            return True
        
        return False
        
            
    yesCount = 0
    yesBool = False
    noCount = 0
    noBool = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                yesCount += 1
                if finished(i,j):
                    yesBool = True
            elif board[i][j] == "X":
                noCount += 1
                if finished(i,j):
                    noBool = True
    if yesCount < noCount:
        return 0
    elif yesBool and yesCount != noCount + 1:
        return 0
    elif noBool and yesCount != noCount:
        return 0 
    elif yesCount - noCount >= 2:
        return 0
    return 1