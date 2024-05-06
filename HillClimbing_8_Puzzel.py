def print_puzzle_state(state):
    for row in state:
        print("-----------------------------")
        for tile in row:
            print("|   {}   |".format(tile), end=" ")
        print()  # Move to the next line after each row
    print("-----------------------------\n\n")

def find_zero_index(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)

def possible_moves(i, j):
    actions_domain = [1, 2, 3, 4]
    if i == 0:
        actions_domain.remove(3)
    elif i == 2:
        actions_domain.remove(4)
    if j == 0:
        actions_domain.remove(1)
    elif j == 2:
        actions_domain.remove(2)
    return actions_domain

import copy

def possible_state(state, move, i, j):
    state_copy = copy.deepcopy(state)
    if move == 1:
        state_copy[i][j], state_copy[i][j - 1] = state_copy[i][j - 1], state_copy[i][j]
    elif move == 2:
        state_copy[i][j], state_copy[i][j + 1] = state_copy[i][j + 1], state_copy[i][j]
    elif move == 3:
        state_copy[i][j], state_copy[i - 1][j] = state_copy[i - 1][j], state_copy[i][j]
    elif move == 4:
        state_copy[i][j], state_copy[i + 1][j] = state_copy[i + 1][j], state_copy[i][j]
    return state_copy

def heuristic(state, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                h = h + 1
    return h

def create_path(CLOSED):
    for state_pair in CLOSED:
        s = state_pair[0]
        print_puzzle_state(s)

OPEN = []
CLOSED = []

def simple_hill_climb(initial_state, goal_state):
    OPEN = []
    CLOSED = []
    h = heuristic(initial_state, goal_state)
    OPEN.append((initial_state, None, h))  # searchNode=(currentState,parentState, heuristicValue)
    
    while OPEN:
        state_pair = OPEN.pop()
        CLOSED.append(state_pair)
        
        state = state_pair[0]  # child node only
        old_h = state_pair[2]  # heuristic value of current state
        
        if state == goal_state:
            print("Goal state reached.")
            # print the path taken
            create_path(CLOSED)
            return True
        
        (i, j) = find_zero_index(state)  # stores the index of zero index in the current state
        for move in possible_moves(i, j):
            new_state = possible_state(state, move, i, j)
            new_h = heuristic(new_state, goal_state)
            if new_h < old_h:  # heuristic needs to decrease
                OPEN.append((new_state, state, new_h))
                
    print("Goal state not found")
    return False

initial_state = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
final_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

simple_hill_climb(initial_state, final_state)
