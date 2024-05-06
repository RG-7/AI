import copy

def enqueue(q, val):
    q.append(val)
    return q

def heuristic(s, g):
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != g[i][j]:
                d += 1
    return d

def dequeue(q):
    return q.pop(0)

def empty_tile(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == 0:
                return [i, j]

def move_up(mat):
    l = empty_tile(mat)
    mat1 = copy.deepcopy(mat)
    i, j = l[0], l[1]
    if i != 0:
        mat1[i][j], mat1[i-1][j] = mat1[i-1][j], mat1[i][j]
        return mat1
    else:
        return None

def move_down(mat):
    l = empty_tile(mat)
    mat1 = copy.deepcopy(mat)
    i, j = l[0], l[1]
    if i != 2:
        mat1[i][j], mat1[i+1][j] = mat1[i+1][j], mat1[i][j]
        return mat1
    else:
        return None

def move_left(mat):
    l = empty_tile(mat)
    mat1 = copy.deepcopy(mat)
    i, j = l[0], l[1]
    if j != 0:
        mat1[i][j], mat1[i][j-1] = mat1[i][j-1], mat1[i][j]
        return mat1
    else:
        return None

def move_right(mat):
    l = empty_tile(mat)
    mat1 = copy.deepcopy(mat)
    i, j = l[0], l[1]
    if j != 2:
        mat1[i][j], mat1[i][j+1] = mat1[i][j+1], mat1[i][j]
        return mat1
    else:
        return None

def breathfirst_search(s, g):
    q = []
    visited = set()
    visited.add(tuple(map(tuple, s)))
    q.append((s, heuristic(s, g)))
    
    while q:
        mat, _ = dequeue(q)
        print("Current State:")
        print_state(mat)
        if mat == g:
            print("Found")
            return
        
        new = move_up(mat)
        if new and tuple(map(tuple, new)) not in visited:
            visited.add(tuple(map(tuple, new)))
            q = enqueue(q, (new, heuristic(new, g)))

        new = move_down(mat)
        if new and tuple(map(tuple, new)) not in visited:
            visited.add(tuple(map(tuple, new)))
            q = enqueue(q, (new, heuristic(new, g)))

        new = move_right(mat)
        if new and tuple(map(tuple, new)) not in visited:
            visited.add(tuple(map(tuple, new)))
            q = enqueue(q, (new, heuristic(new, g)))

        new = move_left(mat)
        if new and tuple(map(tuple, new)) not in visited:
            visited.add(tuple(map(tuple, new)))
            q = enqueue(q, (new, heuristic(new, g)))
    
    print("Not found")

def print_state(mat):
    for row in mat:
        print(row)
    print()

s = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
breathfirst_search(s, g)
# End
