from collections import deque

# Function to perform BFS to find the solution and print the path
def water_jug_bfs(capacities, target):
    visited = set()
    queue = deque([(0, 0, [])])  # Start with empty jugs
    visited.add((0, 0))

    while queue:
        current_state, path = queue.popleft()
        if current_state == target:
            print("Solution path:", path)
            return True  # Solution found
        for next_state in generate_states(current_state, capacities):
            if next_state not in visited:
                visited.add(next_state)
                next_path = path + [next_state]
                queue.append((next_state, next_path))
    return False  # Solution not found

# Example usage
capacities = (3, 5)  # Capacity of jug 1 and jug 2
target = (0, 4)      # Target amount of water in jug 2
print("For BFS:")
if water_jug_bfs(capacities, target):
    print("Solution exists.")
else:
    print("Solution does not exist.")
