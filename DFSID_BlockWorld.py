class BlockWorld:
    depth = 0  

    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = ['move', 'stack', 'unstack']
        self.found_depth = 0 

    def successors(self, state):
        successors = []
        for action in self.actions:
            for i, block_stack in enumerate(state):
                if action == 'move':
                    for j, dest_stack in enumerate(state):
                        if i != j and block_stack:  
                            successors.append(self.apply_move(state, i, j))
                elif action == 'stack':
                    for j, dest_stack in enumerate(state):
                        if i != j and (not dest_stack or (block_stack and dest_stack[-1] > block_stack[-1])):  
                            successors.append(self.apply_stack(state, i, j))
                elif action == 'unstack':
                    if block_stack:  
                        successors.append(self.apply_unstack(state, i))
        return successors

    def apply_move(self, state, source_index, destination_index):
        new_state = [list(stack) for stack in state]  
        block = new_state[source_index].pop()  
        new_state[destination_index].append(block)  
        return new_state

    def apply_stack(self, state, source_index, destination_index):
        new_state = [list(stack) for stack in state]  
        if new_state[source_index]: 
            block = new_state[source_index].pop()  
            new_state[destination_index].append(block)  
        return new_state

    def apply_unstack(self, state, source_index):
        new_state = [list(stack) for stack in state] 
        block = new_state[source_index].pop()  
        new_state.append([block])  
        return new_state

    def is_goal(self, state):
        return state == self.goal_state

    def dfsid(self, current_state, depth, visited):
        if current_state == self.goal_state:
            return [current_state], self.depth  

        if depth <= 0:
            return None, self.found_depth  

        visited.add(tuple(map(tuple, current_state)))  

        for successor in self.successors(current_state):
            if tuple(map(tuple, successor)) not in visited:
                path, found_depth = self.dfsid(successor, depth - 1, visited)
                if path:
                    return [current_state] + path, found_depth

        return None, self.found_depth  

    @classmethod
    def update_depth(cls, new_depth):
        cls.depth = new_depth  

    def solve(self):
        self.update_depth(1)  
        while True:
            visited = set()
            path, found_depth = self.dfsid(self.initial_state, self.depth, visited)
            if path:
                self.found_depth = found_depth  
                return path, found_depth
            self.update_depth(self.depth + 1)  

# Define initial and goal states
initial_state = [['A'], ['B', 'C'], []]
goal_state = [['A', 'B', 'C'], [], []]

# Create BlockWorld instance
block_world = BlockWorld(initial_state, goal_state)

# Solve the problem
solution, found_depth = block_world.solve()

# Print solution if found
if solution:
    for state in solution:
        print(state)
    print("Goal found at depth:", found_depth)
else:
    print("No solution found.")
