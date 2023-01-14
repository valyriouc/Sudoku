import os 
import random 

def init_board(board):
    pass

def update_board(board, input):
    y,x = input[0] - 1, input[1] - 1
    if (board[y][x] == 'X'):
        board[y][x] = input[2]

def draw(board):
    os.system('cls')
    for y in range(0, 9):
        if (y == 0):
            print("  ", end="")
            for i in range(1, 10):
                print(i, end=" ")
            print()
        for x in range(0, 9):
            if (x == 0):
                print(y+1, end=" ")
            print(board[y][x], end=" ")
        print()

def get_input():
    # TODO Implement check for invalid field input formatting 
    field = input("Please type in the field you want to select (y/x): ").split("/")
    y, x= int(field[0]), int(field[1])
    if (x < 1 or x > 9 or y < 1 or y > 9):
        raise ValueError("Value for x and y must between 1 and 9")
    
    number = int(input("Type in the number you want to put into the field (1-9)"))
    if (number < 1 or number > 9):
        raise ValueError("Number must between 1 and 9!")
    
    return (y, x, number)

def check_board(board):
    pass

if __name__ == '__main__':  
    
    # variables 
    board = [['X' for x in range(0, 9)] for y in range(0, 9)] 
    tries = 3
    isRunning = True
    
    init_board(board)
    
    while isRunning:
        try: 
            draw(board)
            data = get_input()
            update_board(board, data)
        except ValueError:
            continue
        
