# TSP (Traverse Salesman Problem
# Travelling Salesman Problem
import itertools
V=4

def calculate_total_distance(route, matrix):
    total_distance = 0
    for i in range(V - 1):
        total_distance += matrix[route[i]][route[i + 1]]
    total_distance += matrix[route[-1]][route[0]]
    return total_distance
    
    
def travellingSalesmanProblem(matrix):
    vertex = list(range(V))
    all_possible = list(itertools.permutations(vertex))
    print(all_possible)
    
    min_distance = float('inf')
    best_route = None
    for perm in all_possible:
        current_distance = calculate_total_distance(perm, matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = perm

    print("Best Route:")
    for vertex in best_route:
        print(vertex, end=" -> ")
    print(best_route[0]) 
    
    print("Minimum Distance:", min_distance)

matrix = [[0,15,10,20],[15,0,20,10],[10,20,0,15],[20,10,15,0]]

travellingSalesmanProblem(matrix)
