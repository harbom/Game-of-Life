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

#tests the render function which prints the board to the screen
def test_render():
    dead_test = dead_state(width,height)
    render(dead_test)

    random_test = random_state(width,height)
    render(random_test)

#calculates the next state of the board
def next_board_state(board):
    next_board = board #this array will store boolean values and update after population

    #iterate over board and check for conditions
    width = len(board[0])
    height = len(board)

    for i in range(height):
        for j in range(width):
            # any live cell with 0 or 1 neighbors -->  dead
            # any live cell with 2 or 3 live neighbors stays alive
            # any live cell with > 3 live neighbors --> dead
            # any dead cell with 4 neightbors --> alive
            
            neighbors = [None,None,None,None] #in order of left_neighbor, top_neighbor, bottom_neighbor, right_neighbor, not like it actually matters
            
            if board[i][j]==0: #cell is dead
                pass
            else: #cell is alive
                pass

def main():
    board = random_state(width,height)


if __name__ == '__main__':
    main()