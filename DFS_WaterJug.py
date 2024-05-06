# Function to generate all possible states by pouring water
def generate_states(state, capacities):
    states = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j:
                new_state = state.copy()
                amount_to_pour = min(state[i], capacities[j] - state[j])
                new_state[i] -= amount_to_pour
                new_state[j] += amount_to_pour
                states.append(new_state)
    return states

# Function to perform DFS to find the solution
def water_jug_dfs_helper(state, target, capacities, visited, path):
    if state == target:
        print("Solution path:", path)
        return True  # Solution found
    visited.add(state)
    for next_state in generate_states(state, capacities):
        if next_state not in visited:
            next_path = path + [next_state]
            if water_jug_dfs_helper(next_state, target, capacities, visited, next_path):
                return True
    return False

def water_jug_dfs(capacities, target):
    visited = set()
    return water_jug_dfs_helper((0, 0), target, capacities, visited, [(0, 0)])

# Example usage
capacities = (3, 5)  # Capacity of jug 1 and jug 2
target = (0, 4)      # Target amount of water in jug 2
print("For DFS:")
if water_jug_dfs(capacities, target):
    print("Solution exists.")
else:
    print("Solution does not exist.")
