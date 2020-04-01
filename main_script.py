import numpy as np

width = 8
height = 5

#initializes a blank board with 0's
def dead_state(width,height):
    return np.zeros([height,width])

#randomizes the board 
def random_state(width,height):
    state = dead_state(width,height)

    for i in range(height):
        for j in range(width):
            state[i][j] = np.random.randint(2)
    
    return state

def render(board):
    board_width = len(board[0]) + 2 #adding another character on to each end
    board_height = len(board) + 2 #adding another character on to each end

    #print top of board
    print('- '*board_width)

    #print the array
    for array in board:
        print("|",end=" ")
        for spot in array:
            if (spot == 0):
                print(" ",end=" ")
            else:
                print("∎",end=" ")
        print("|")
    
    #print bottom of board
    print('- '*board_width)

def test_render():
    dead_test = dead_state(width,height)
    render(dead_test)

    random_test = random_state(width,height)
    render(random_test)

def main():
    test_render()

if __name__ == '__main__':
    main()