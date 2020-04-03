import time
import random
import numpy as np

prog_width=20
prog_height=5
#initializes a blank board with 0's
def dead_state(width,height):
    subarray = [0]*width
    result=[]
    for i in range(height):
        result.append(subarray)

    return result

#randomizes the board 
def random_state(width,height):
    state = []

    for i in range(height):
        temp_arr=[]
        for j in range(width):
            temp_arr.append(np.random.randint(2))
        state.append(temp_arr)

    return state

def render(board):
    board_width = len(board[0])
    board_height = len(board)

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
    dead_test = dead_state(prog_width,prog_height)
    render(dead_test)

    random_test = random_state(prog_width,prog_height)
    render(random_test)

def check_neighbors(board,neighbors,i,j,width,height):
    #assign the neighbors, with wraparound
    #left
    if (j!=0):
        neighbors[0] = board[i][j-1]
    else:
        neighbors[0] = board[i][-1]
    #top
    if i!= 0:
        neighbors[1] = board[i-1][j]
    else:
        neighbors[1] = board[-1][j]
    #bottom
    if i<height-1:
        neighbors[2] = board[i+1][j]
    else:
        neighbors[2] = board[0][j]
    #right
    if j<width-1:
        neighbors[3] = board[i][j+1]
    else:
        neighbors[3] = board[i][0]
    
    #top-left
    if j != 0 and i != 0:
        neighbors[4] = board[i-1][j-1]
    else:
        if j!=0 and i== 0: #if its on the first row but not on left
            neighbors[4] = board[-1][j-1]
        elif j==0 and i!=0: #if on the left but not on first row
            neighbors[4] = board[i-1][-1]
        else: #in the top left box
            neighbors[4] = board[-1][-1]

    #bottom-left
    if j != 0 and i < height - 1:
        neighbors[5] = board[i+1][j-1]
    else:
        if j==0 and i<height-1: #on left col but not on bottom row
            neighbors[5] = board[i+1][-1]
        elif j!=0 and i>=height-1: #on bottom row but not left col
            neighbors[5] = board[0][j-1]
        else: #on bottom left corner
            neighbors[5] = board[0][-1]
    
    #top-right
    if j < width -1 and i != 0:
        neighbors[6] = board[i-1][j+1]
    else:
        if j<width-1 and i==0: #on top row but not right
            neighbors[6] = board[-1][j+1]
        elif j>=width-1 and i!=0: #on right col but not top
            neighbors[6] = board[i-1][0]
        else: #on top right box
            neighbors[6] = board[-1][0]

    #bottom-right
    if j < width - 1 and i < height - 1:
        neighbors[7] = board[i+1][j+1]
    else:
        if j>=width-1 and i<height-1: #on right col but not last row
            neighbors[7] = board[i+1][0]
        elif j<width-1 and i>=height-1: #on bottom row but not on right col
            neighbors[7] = board[0][j+1]
        else: #on bottom right box
            neighbors[7] = board[0][0]


#calculates the next state of the board
def next_board_state(board):
    width=len(board[0])
    height=len(board)

    next_board = []

    #iterate over board and check for conditions
    for i in range(0,height):
        new_arr = []
        for j in range(0,width):
            # any live cell with 0 or 1 live neighbors -->  dead
            # any live cell with 2 or 3 live neighbors stays alive
            # any live cell with > 3 live neighbors --> dead
            # any dead cell with 3 neightbors --> alive
            
            neighbors = [None,None,None,None,None,None,None,None]
            
            #assign the neighbors, with wraparound
            #left
            if (j!=0):
                neighbors[0] = board[i][j-1]
            else:
                neighbors[0] = board[i][-1]
            #top
            if i!= 0:
                neighbors[1] = board[i-1][j]
            else:
                neighbors[1] = board[-1][j]
            #bottom
            if i<height-1:
                neighbors[2] = board[i+1][j]
            else:
                neighbors[2] = board[0][j]
            #right
            if j<width-1:
                neighbors[3] = board[i][j+1]
            else:
                neighbors[3] = board[i][0]
            
            #top-left
            if j != 0 and i != 0:
                neighbors[4] = board[i-1][j-1]
            else:
                if j!=0 and i== 0: #if its on the first row but not on left
                    neighbors[4] = board[-1][j-1]
                elif j==0 and i!=0: #if on the left but not on first row
                    neighbors[4] = board[i-1][-1]
                else: #in the top left box
                    neighbors[4] = board[-1][-1]

            #bottom-left
            if j != 0 and i < height - 1:
                neighbors[5] = board[i+1][j-1]
            else:
                if j==0 and i<height-1: #on left col but not on bottom row
                    neighbors[5] = board[i+1][-1]
                elif j!=0 and i>=height-1: #on bottom row but not left col
                    neighbors[5] = board[0][j-1]
                else: #on bottom left corner
                    neighbors[5] = board[0][-1]
            
            #top-right
            if j < width -1 and i != 0:
                neighbors[6] = board[i-1][j+1]
            else:
                if j<width-1 and i==0: #on top row but not right
                    neighbors[6] = board[-1][j+1]
                elif j>=width-1 and i!=0: #on right col but not top
                    neighbors[6] = board[i-1][0]
                else: #on top right box
                    neighbors[6] = board[-1][0]

            #bottom-right
            if j < width - 1 and i < height - 1:
                neighbors[7] = board[i+1][j+1]
            else:
                if j>=width-1 and i<height-1: #on right col but not last row
                    neighbors[7] = board[i+1][0]
                elif j<width-1 and i>=height-1: #on bottom row but not on right col
                    neighbors[7] = board[0][j+1]
                else: #on bottom right box
                    neighbors[7] = board[0][0]
            
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
                    new_arr.append(1)#next_board[i][j] = 1 #revives
                else:
                    new_arr.append(0)#next_board[i][j] = 0 #stays dead
            else: #cell is alive
                if num_alive == 2 or num_alive == 3:
                    new_arr.append(1)#next_board[i][j] = 1 #stays alive
                else:
                    new_arr.append(0)#next_board[i][j] = 0 #dies
        
        next_board.append(new_arr)
        
    
    return next_board

def test_next_board():
    board = random_state(prog_width,prog_height)
    next_board = next_board_state(board)
    
    print("before: ")
    render(board)
    print("after: ")
    render(next_board)

def random_run():
    curr = random_state(prog_width,prog_height)
    while (True):
        render(curr)
        curr = next_board_state(curr)
        print()
        time.sleep(1)

def read_from_file():
    filename = "preloaded_states/gosper_glider_gun.txt"
    reader = open(filename,"r")
    contents = reader.readlines()
    
    board = []
    for i in range(len(contents)):
        curr_string = contents[i][0:-1]
        if i == len(contents)-1:
            curr_string += '0'
        new_int_arr = []
        for j in curr_string:
            new_int_arr.append(int(j))
        
        board.append(new_int_arr)
    
    while(True):
        render(board)
        board = next_board_state(board)
        print()
        time.sleep(.1)

def main():
    #random_run()
    read_from_file()

if __name__ == '__main__':
    main()