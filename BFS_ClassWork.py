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
