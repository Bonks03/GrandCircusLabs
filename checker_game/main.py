import checkers as chk

def game():
    while True:
        size = int(input('Please enter the size of your board (4-16): '))
        if 4 <= size <= 16:
            break
    board = chk.build_board(size)
    print(board)
    for i in ['red', 'black', 'empty']:
        print(f'There are {chk.get_count(board, i)} {i.capitalize()} cells.')

if __name__ == '__main__':
    game()