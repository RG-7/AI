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

def heuristic_val(s,curr_state,g):
    heur_val = heuristic(s,curr_state) + heuristic(g,curr_state)
    return heur_val

def astar_search(s,g):
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
                    q.append((new,heuristic_val(s,new,g)))

        new = move_down(curr_state)
        if new != curr_state:
            if new == g:
              print("found")
              return
            else:
                if new not in visited:
                    q.append((new,heuristic_val(s,new,g)))

        new = move_right(curr_state)
        if new != curr_state:
            if new == g:
              print("found")
              return
            else:
                if new not in visited:
                    q.append((new,heuristic_val(s,new,g)))

        new = move_left(curr_state)
        if new != curr_state:
            if new == g:
              print("found")
              return
            else:
                if new not in visited:
                    q.append((new,heuristic_val(s,new,g)))

        if len(q) > 0:
            t = deque()
            curr_state=t[0]
            q=t[1]
        else:
            print ("not found")
            return

import copy
s = [[2,0,3],[1,8,4],[7,6,5]]
g = [[1,2,3],[8,0,4],[7,6,5]]
global q
q=[]
global visited
visited=[]
visited = visited + [s]
astar_search(s,g)
