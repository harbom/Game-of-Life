from main_script import next_board_state
from main_script import check_neighbors

def main():
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0,0,0,0],
        [0,1,1,0,0,0],
        [0,1,1,0,0,0],
        [0,0,0,1,1,0],
        [0,0,0,1,1,0],
        [0,0,0,0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0,0,0,0],
        [0,1,1,0,0,0],
        [0,1,0,0,0,0],
        [0,0,0,0,1,0],
        [0,0,0,1,1,0],
        [0,0,0,0,0,0]
    ]
    actual_next_state1 = next_board_state(init_state1)

    print("passed")
    print( "Expected:")
    for i in range(len(expected_next_state1)):
        print(expected_next_state1[i])
    print( "Actual:")
    print( actual_next_state1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
    ]
    expected_next_state2 = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    actual_next_state2 = next_board_state(init_state2)

    print( "Expected:")
    for i in range(len(expected_next_state2)):
        print(expected_next_state2[i])
    print( "Actual:")
    print( actual_next_state2)

if __name__ == "__main__":
    main()