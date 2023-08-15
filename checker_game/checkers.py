from numpy import zeros
from numpy import random as rdm

def build_board(board_size):
    board = zeros((board_size, board_size), str)
    for i in range(board_size):
        for j in range(board_size):
            board[i, j] = rdm.choice(['R', 'B', 'E'])
    return board

def get_count(board, color):
    count = 0
    color = color[0].upper()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i, j] == color:
                count += 1
    return count

if __name__ == '__main__':
    print('This is not supposed to run as main.')