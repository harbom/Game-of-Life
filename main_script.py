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
    next_board = board

    #iterate over board and check for conditions
    width = len(board[0])
    height = len(board)

    for i in range(height):
        for j in range(width):
            # any live cell with 0 or 1 neighbors -->  dead
            # any live cell with 2 or 3 live neighbors stays alive
            # any live cell with > 3 live neighbors --> dead
            # any dead cell with 4 neightbors --> alive
            
            neighbors = [None,None,None,None] #in order of left_neighbor, top_neighbor, bottom_neighbor, right_neighbor
            
            #assign the neighbors, if they exist
            #check for left_neighbor
            if j != 0:
                neighbors[0] = board[i][j-1]
            #check for top_neighbor
            if i != 0:
                neighbors[1] = board[i-1][j]
            #check for bottom_neightbor
            if i != height-1:
                neighbors[2] = board[i+1][j]
            #check for right neighbor
            if j != width-1:
                neighbors[3] = board[i][j+1]
            
            #count up num alive and dead
            num_alive = 0
            num_dead = 0
            for i in neighbors:
                if i==0:
                    num_dead += 1
                else:
                    num_alive += 1

            #update value
            if board[i][j]==0: #cell is dead
                if num_alive == 4:
                    next_board[i][j] = 1 #revives
                else:
                    next_board[i][j] = 0 #stays dead
            else: #cell is alive
                if num_alive == 2 or num_alive == 3:
                    next_board[i][j] = 1 #stays alive
                else:
                    next_board[i][j] = 0 #dies
        
        return next_board

def main():
    board = random_state(width,height)


if __name__ == '__main__':
    main()