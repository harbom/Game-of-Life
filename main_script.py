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

    #print the array
    for array in board:
        for spot in array:
            if (spot == 0):
                print("□",end=" ")
            else:
                print("∎",end=" ")
        print()

#tests the render function which prints the board to the screen
def test_render():
    dead_test = dead_state(width,height)
    render(dead_test)

    random_test = random_state(width,height)
    render(random_test)

#calculates the next state of the board
def next_board_state(board):
    width=len(board[0])
    height=len(board)

    next_board = dead_state(width,height)

    #iterate over board and check for conditions
    for i in range(0,height):
        for j in range(0,width):
            # any live cell with 0 or 1 live neighbors -->  dead
            # any live cell with 2 or 3 live neighbors stays alive
            # any live cell with > 3 live neighbors --> dead
            # any dead cell with 3 neightbors --> alive
            
            neighbors = [None,None,None,None,None,None,None,None]
            
            #assign the neighbors, if they exist
            #left
            if j != 0:
                neighbors[0] = board[i][j-1]
            #top
            if i != 0:
                neighbors[1] = board[i-1][j]
            #bottom
            if i < height - 1:
                neighbors[2] = board[i+1][j]
            #right
            if j < width - 1:
                neighbors[3] = board[i][j+1]
            #top-left
            if j != 0 and i != 0:
                neighbors[4] = board[i-1][j-1]
            #bottom-left
            if j != 0 and i < height - 1:
                neighbors[5] = board[i+1][j-1]
            #top-right
            if j < width -1 and i != 0:
                neighbors[6] = board[i-1][j+1]
            #bottom-right
            if j < width - 1 and i < height - 1:
                neighbors[7] = board[i+1][j+1]
            
            #count up num alive and dead
            num_alive = 0
            num_dead = 0
            for f in neighbors:
                if f==0:
                    num_dead += 1
                elif f==1:
                    num_alive += 1

            #update value
            if board[i][j] == 0: #cell is dead
                if num_alive == 3:
                    next_board[i][j] = 1 #revives
                else:
                    next_board[i][j] = 0 #stays dead
            else: #cell is alive
                if num_alive == 2 or num_alive == 3:
                    next_board[i][j] = 1 #stays alive
                else:
                    next_board[i][j] = 0 #dies
        
    
    return next_board

def test_next_board():
    board = random_state(width,height)
    next_board = next_board_state(board)
    
    print("before: ")
    render(board)
    print("after: ")
    render(next_board)

def main():
    test_next_board()


if __name__ == '__main__':
    main()