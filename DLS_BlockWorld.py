# Depth Limit Search
from collections import deque

def actions(state):
    possible_actions = []
    if len(state[0]) > 0:
        possible_actions.append(1)
    
    if len(state[1]) > 0:
        possible_actions.append(2)
    
    if len(state[2]) > 0:
        possible_actions.append(3)
    
    return possible_actions

import copy

def create_states(state, action):
    state_copy1 = copy.deepcopy(state)
    state_copy2 = copy.deepcopy(state)
    
    new_states = []
    
    if action == 1:
        top_block = state_copy1[0].pop()
        top_block = state_copy2[0].pop()
        state_copy1[1].append(top_block)
        state_copy2[2].append(top_block)
        
    elif action == 2:
        top_block = state_copy1[1].pop()
        top_block = state_copy2[1].pop()
        state_copy1[0].append(top_block)
        state_copy2[2].append(top_block)
        
    elif action == 3:
        top_block = state_copy1[2].pop()
        top_block = state_copy2[2].pop()
        state_copy1[0].append(top_block)
        state_copy2[1].append(top_block)
        
    new_states.append(state_copy1)
    new_states.append(state_copy2)
    
    return new_states

def print_path(path):
    for state in path:
        print(state)
        
def get_parent(state, CLOSED):
    for (c, p, d) in CLOSED:
        if state == c:
            return p

def create_path(goal_state, CLOSED):
    my_path = [goal_state]
    
    p = get_parent(goal_state, CLOSED)
    while p != None:  
        my_path.append(p)
        p = get_parent(p, CLOSED)
        
    return my_path

def check_unique(OPEN, CLOSED, new_state):
    my_list = list(OPEN) + CLOSED # merge both lists
    for (child, parent, depth) in my_list:
        if set(tuple(element) for element in child) == set(tuple(element) for element in new_state):
            return False
        
    return True

def depth_limited_search(initial_state, goal_state, MAX_DEPTH):
    OPEN_stack = deque()
    CLOSED = []
    depth = 0
    
    OPEN_stack.append((initial_state, None, 0))
    while OPEN_stack:
        state_pair = OPEN_stack.pop()  
        CLOSED.append(state_pair)
        
        state = state_pair[0]  
        depth = state_pair[2]  

        if state == goal_state:
            print("Goal state reached.")
            solution_path = create_path(goal_state, CLOSED)
            print_path(solution_path)
            return True

        if depth < MAX_DEPTH:
            for action in actions(state):
                new_states = create_states(state, action)
                for new_state in new_states:
                    if check_unique(OPEN_stack, CLOSED, new_state):
                        OPEN_stack.append((new_state, state, depth+1))
    
    print("Goal state not found")
    return False

# Initial state of blocks
initial_state = [['A'], ['B', 'C'], []]
# Goal state of blocks
goal_state = [['A', 'B', 'C'], [], []]
# Maximum depth limit for DLS
MAX_DEPTH = 3

depth_limited_search(initial_state, goal_state, MAX_DEPTH)
