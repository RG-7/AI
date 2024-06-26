# Day 7
# February 20, 2024
# Assignment 3
import copy
from collections import deque

def generate_children(s):
    l = []
    for i in range(len(s)):
        if len(s[i]) != 0:
            for j in range(len(s)):
                s1 = copy.deepcopy(s)
                if j != i:
                    x = s1[i][0]
                    s1[i].remove(x)
                    s1[j].insert(0, x)
                    l.append(s1)
    return l

def bfs(initial_state, goal_state):
    queue = deque([initial_state])
    visited = set()
    while queue:
        current_state = queue.popleft()
        if tuple(map(tuple, current_state)) not in visited:
            print("Current state:", current_state)
            visited.add(tuple(map(tuple, current_state)))
            if current_state == goal_state:
                return current_state
            children = generate_children(current_state)
            queue.extend(children)

initial_state = [[1,2], [3], []]
goal_state = [[], [2,3], [1]]

print("Initial state:", initial_state)
print("Goal state:", goal_state)


print("\nBFS:")
result_bfs = bfs(initial_state, goal_state)
print("Result_BFS:", result_bfs)

