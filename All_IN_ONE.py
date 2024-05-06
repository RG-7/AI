import copy

def enqueue(s,val):
    q.append((val,s))
    return q

def heuristic(s,g):
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != g[i][j]:
                d += 1
    return d

def deque():
    global q
    new=[]
    for each in q:
        new.append(each[1])
    new.sort()
    for each in q:
        if(each[1]==new[0]):
            elem=each[0]
            print("elem",elem)
            break
    q.remove((elem,each[1]))
    return ((elem,q))

def empty_tile(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j]==0:
                return([i,j])

def move_up(mat):
    l=empty_tile(mat)
    mat1=copy.deepcopy(mat)
    i=l[0]
    j=l[1]
    if i!=0:
        mat1[i][j],mat1[i-1][j]=mat1[i-1][j],mat1[i][j]
        return mat1
    else:
        return mat

def move_down(mat):
    l=empty_tile(mat)
    mat1=copy.deepcopy(mat)
    i=l[0]
    j=l[1]
    if i!=2:
        mat1[i][j],mat1[i+1][j]=mat1[i+1][j],mat1[i][j]
        return mat1
    else:
        return mat

def move_left(mat):
    l=empty_tile(mat)
    i=l[0]
    j=l[1]
    mat1=copy.deepcopy(mat)
    if j!=0:
        mat1[i][j],mat1[i][j-1]=mat1[i][j-1],mat1[i][j]
        return mat1
    else:
        return mat

def move_right(mat):
    l=empty_tile(mat)
    mat1=copy.deepcopy(mat)
    i=l[0]
    j=l[1]
    if j!=2:
        mat1[i][j],mat1[i][j+1]=mat1[i][j+1],mat1[i][j]
        return mat1
    else:
        return mat

def bestfs_search(mat,g):
    global q
    global visited
    visited=[]
    q=[]
    visited.append(mat)
    while(1):
        new = move_up(mat)
        val=heuristic(new,g)
        if new != mat:
            if new == g:
                print ("found")
                return
            else:
                if new not in visited:
                    q.append((new,val))

        new = move_down(mat)
        val=heuristic(new,g)
        if new != mat:
            if new == g:
                print ("found")
                return
            else:
                if new not in visited:
                    q.append((new,val))
        new = move_right(mat)
        val=heuristic(new,g)
        if new != mat:
            if new == g:
                print ("Found")
                return
            else:
                if new not in visited:
                    q.append((new,val))
        new = move_left(mat)
        val=heuristic(new,g)
        if new != mat:
            if new == g:
                print ("Found")
                return
            else:
                if new not in visited:
                    q.append((new,val))
                    print(new)
        if len(q) > 0:
            t = deque()
            mat=t[0]
            q=t[1]
            if mat not in visited:
                visited.append(mat)
        else:
            print ("not found")
            return

def heuristic_val(s, curr_state, g):
    heur_val = heuristic(s, curr_state) + heuristic(g, curr_state)
    return heur_val

def astar_search(s, g):
    curr_state = copy.deepcopy(s)
    if s == g:
        return
    global visited
    global q
    visited=[]
    q=[]
    while(1):
        new = move_up(curr_state)
        if new != curr_state:
            if new == g:
                print("found")
                return
            else:
                if new not in visited:
                    q.append((new, heuristic_val(s, new, g)))

        new = move_down(curr_state)
        if new != curr_state:
            if new == g:
                print("found")
                return
            else:
                if new not in visited:
                    q.append((new, heuristic_val(s, new, g)))

        new = move_right(curr_state)
        if new != curr_state:
            if new == g:
                print("found")
                return
            else:
                if new not in visited:
                    q.append((new, heuristic_val(s, new, g)))

        new = move_left(curr_state)
        if new != curr_state:
            if new == g:
                print("found")
                return
            else:
                if new not in visited:
                    q.append((new, heuristic_val(s, new, g)))

        if len(q) > 0:
            t = deque()
            curr_state=t[0]
            q=t[1]
        else:
            print ("not found")
            return

def Cost(H, path, weight=1):
    cost = {}
    if 'AND' in path:
        AND_nodes = path['AND']
        Path_A = ' AND '.join(AND_nodes)
        PathA = sum(H[node] + weight for node in AND_nodes)
        cost[Path_A] = PathA

    if 'OR' in path:
        OR_nodes = path['OR']
        Path_B = ' OR '.join(OR_nodes)
        PathB = min(H[node] + weight for node in OR_nodes)
        cost[Path_B] = PathB
    return cost

def update_cost(H, paths, weight=1):
    Main_nodes = list(paths.keys())
    Main_nodes.reverse()
    least_cost = {}
    for key in Main_nodes:
        path = paths[key]
        print(key, ':', paths[key], '>>>', Cost(H, path, weight))
        c = Cost(H, path, weight)
        H[key] = min(c.values())
        least_cost[key] = Cost(H, path, weight)
    return least_cost

def shortest_path(Start, Updated_cost, G):
    Path = Start
    if Start in Updated_cost.keys():
        Min_cost = min(Updated_cost[Start].values())
        key = list(Updated_cost[Start].keys())
        values = list(Updated_cost[Start].values())
        Index = values.index(Min_cost)

        Next = key[Index].split()
        if len(Next) == 1:
            Start = Next[0]
            Path += '<--' + shortest_path(Start, Updated_cost, G)
        else:
            Path += '<--(' + key[Index] + ') '

            Start = Next[0]
            Path += '[' + shortest_path(Start, Updated_cost, G) + ' + '

            Start = Next[-1]
            Path += shortest_path(Start, Updated_cost, G) + ']'

    return Path

G = {'A': -1, 'B': 5, 'C': 2, 'D': 4, 'E': 7, 'F': 9, 'G': 3, 'H': 0, 'I':0, 'J':0}

paths = {
    'A': {'OR': ['B'], 'AND': ['C', 'D']},
    'B': {'OR': ['E', 'F']},
    'C': {'OR': ['G'], 'AND': ['H', 'I']},
    'D': {'OR': ['J']}
}

weight = 1
print('Updated Cost:')
Updated_cost = update_cost(G, paths, weight=1)
print('Shortest Path:\n', shortest_path('A', Updated_cost, G))
