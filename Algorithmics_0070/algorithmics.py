### ALL ALGORITHMS FROM COMP0070-ALGORITHMICS MODULE ###

# ref - s.11
def OddTest(x):
    if x%2 == 0:
        return 'no'
    else:
        return 'yes'
    
# ref - s.12
def PrintNumberSequence(x):
    n = 0
    while n <= x:
        print(n)
        n += 1
        
# ref - s.13
def PrintPairs(x):
    m = 0
    n = 0
    while n <= x:
        while m <= x:
            print(n,m)
            m += 1
        n += 1
        m = 0
        
# ref - s.14
def multiply1(x,y):
    '''
    Multiplication of x and y by repeated addition.
    '''
    p = 0
    while y != 0:
        p += x
        y -= 1
    return p

# ref - s.16
def multiply2(x,y):
    '''
    Multiplication of x and y by multiplication by two.
    '''
    p = 0
    while y != 0:
        while y % 2 ==0:
            x = x*2
            y = y/2
        p += x
        y = y - 1
    return p

# ref - s.25
def GCD1(m,n):
    '''
    Finding greatest common divisor of m and n by definition.
    '''
    if m == 0 or n == 0:
        i = max([m,n])
    else:
        i = min([m,n]) + 1
    while m%i!=0 or n%i!=0:
        i -= 1
    return i

# ref - s.27
def GCD2(m,n):
    '''
    Finding greatest common divisor of m and n by Euclid' algorithm.
    '''
    while m > 0:
        t = n % m
        n = m
        m = t
    return n

# ref - s.28
def Fibonacci1(n):
    '''
    Returns n-th number in Fibonacci sequence. Exponentially more complex method.
    '''
    if n <= 2:
        return 1
    else:
        return Fibonacci1(n-1) + Fibonacci1(n-2)      
    
# ref - s.30
def Fibonacci2(n):
    '''
    Returns n-th number in Fibonacci sequence. Efficient method.
    '''
    i = 1
    j = 0
    c = 0
    while c < n:
        j += i
        i = j - i
        c += 1
    return j

# ref - s.34
def InsertionSort(Array):
    for j in range(2,len(Array)):
        temp = Array[j]
        i = j - 1
        while i > 0 and Array[i] > temp:
            Array[i+1] = Array[i]
            i -= 1
        Array[i+1] = temp
    return Array

# ref - s.71
def KruskalsAlgo(Matrix,demonstrate=False):
    '''
    A greedy algorithm for finding a minimum spanning tree.

    Input:
        Matrix: an undirected weighted graph in the form of a matrix. (list of lists)
    Output:
        The list of edges to construct the tree and minimum cost.
        If demostrate = True --> then also a table showing when each edge is added to the solution
    '''
    import operator
    import numpy as np
    
    #default test, not part of the method but will make it easier to 
    #later test
    test = [[np.inf, 1, np.inf, 4, np.inf, np.inf, np.inf],
               [1, np.inf, 2, 6, 4, np.inf, np.inf],
               [np.inf, 2, np.inf, np.inf, 5, 6, np.inf],
               [4, 6, np.inf, np.inf, 3, np.inf, 4],
               [np.inf, 4, 5, 3, np.inf, 8, 7],
               [np.inf, np.inf, 6, np.inf, 8, np.inf, 3],
               [np.inf, np.inf, np.inf, 4, 7, 3, np.inf]]
    
    A = []
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if Matrix[i][j]<np.inf:
                if (f'a{j+1}',f'a{i+1}',Matrix[i][j]) not in A:
                    A.append((f'a{i+1}',f'a{j+1}',Matrix[i][j]))
    A = sorted(A, key = operator.itemgetter(2))
    
    T = []
    paths = []
    cost = 0
    for i in range(len(Matrix)):
        T.append([f'a{i+1}'])
        
    if demonstrate:
        step = 0
        print('Step: |Edge considered: |Solution: ')
        print('--------------------------------------')

    for x,y,z in A:
        edge = [x,y]
        a = [i for i in T if x in i or y in i]
        if len(a) == 1:
            continue
        T.remove(a[0])
        T.remove(a[1])
        T.append([i for sublist in a for i in sublist])
        cost += z
        paths.append((x,y,z))
        
        if demonstrate:
            step+=1
            print(step,'    ',(x,y,z),' ',T)
            
        if len(T) == 1:
            break
        
    print('--------------------------------------')
    print(f'Cost of shortest path: {cost} and the path itself is: ') 
    print(paths)

# ref - s.76
def PrimAlgo(Matrix, start='a3', demonstrate=False):
    '''
    A greedy algorithm for finding a minimum spanning tree
    
    Input:
        Matrix: an undirected weighted graph in the form of a matrix. (list of lists)
        start: starting node from which to begin calculating the tree. (str)
    Output:
        The list of edges to construct the tree and minimum cost.
        If demostrate = True --> then also a table showing when each edge is added to the solution.
    '''
    import operator
    import numpy as np
    
    #default test, not part of the method but will make it easier to 
    #later test
    test = [[np.inf, 1, np.inf, 4, np.inf, np.inf, np.inf],
               [1, np.inf, 2, 6, 4, np.inf, np.inf],
               [np.inf, 2, np.inf, np.inf, 5, 6, np.inf],
               [4, 6, np.inf, np.inf, 3, np.inf, 4],
               [np.inf, 4, 5, 3, np.inf, 8, 7],
               [np.inf, np.inf, 6, np.inf, 8, np.inf, 3],
               [np.inf, np.inf, np.inf, 4, 7, 3, np.inf]]
    
    A = []
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if Matrix[i][j]<np.inf:
                A.append((f'a{i+1}',f'a{j+1}',Matrix[i][j]))
    A = sorted(A, key = operator.itemgetter(2))
    
    paths = []
    T = []
    cost = 0
    first = [(i,j,k) for i,j,k in A if i == start][0]
    T.append(first[0])
    T.append(first[1])
    A.remove(first)
    A.remove([(i,j,k) for i,j,k in A if j == start][0])
    paths.append(first)
    cost += first[2]
    
    if demonstrate:
        step = 1
        print('Step: |Edge considered: |Solution: ')
        print('--------------------------------------')
        print(step,'    ',first,' ',T)
        
    while len(T) < 7:
        options = []

        for i in T:
            t = [item for item in T if item != i]
            for j in t:
                try:
                    options.append([(x,y,z) for x,y,z in A if x == j
                                if y not in T][0])
                except:
                    continue
        options = sorted(options, key = operator.itemgetter(2))
        next = options[0]
        paths.append(next)
        cost += next[2]
        T.append(next[1])
        A.remove(next)
        x,y,z = next
        A.remove((y,x,z))
        
        if demonstrate:
            step += 1
            print(step,'    ',next,' ',T)
            
    print('--------------------------------------')
    print(f'Cost of shortest path: {cost} and the path itself is: ') 
    print(paths)   
    
# ref - s.85
def DijkstrasAlgo(Matrix, node='a1', demonstrate=False):
    '''
    A greedy algorithm seeking to form minimum span tree. Solution is constructed incrementally.
    
    Input:
        Matris: weighted directed graph. (list of lists)
        node: designated node.
    Output:
        The cost of the shortest path from the designated node to each of the other nodes.
        If demonstate = True --> also the educational demonstration of each step of the algorithm
    '''
    import operator
    import numpy as np
    
    #default test, not part of the method but will make it easier to 
    #later test
    test = [ [np.inf, 50, 30, 100, 10],
           [np.inf, np.inf, np.inf, np.inf, np.inf],
           [np.inf, 5, np.inf, 50, np.inf],
           [np.inf, 20, np.inf, np.inf, np.inf],
           [np.inf, np.inf, np.inf, 10, np.inf]]
    
    A = []
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if Matrix[i][j]<np.inf:
                A.append((f'a{i+1}',f'a{j+1}',Matrix[i][j]))
    A = sorted(A, key = operator.itemgetter(2))
    
    D = [(x,y,z) for x,y,z in A if x == node]
    C = [y for x,y,z in D]
    
    if demonstrate:
        step = 0
        print('Step:    |v:     |C:                             |D:     ')
        print('---------------------------------------------------------')
        print(step,'\t','-','\t', C,'\t',[z for x,y,z in D])
        
    for turn in range(len(Matrix)-2):
        D_relevant = [(x,y,z) for x,y,z in D if y in C]
        v = D_relevant[0]
        secondary_path = [(x,y,z) for x,y,z in A if x==v[1]][0]
        primary_path = [(x,y,z) for x,y,z in D if y==secondary_path[1]]
        if v[2]+secondary_path[2] < primary_path[0][2]:
            C.remove(v[1])
            D.remove(primary_path[0])
            D.append((node,secondary_path[1],v[2]+secondary_path[2])) 
            D = sorted(D, key = operator.itemgetter(2))
        else:
            continue
        if demonstrate:
            step+=1
            print(step,'\t',v[1],'\t',C,'\t'*(len(Matrix)-len(C)),[z for x,y,z in D])
    print('---------------------------------------------------------')
    print(f'The cost of shortest path is: {sum([z for x,y,z in D])}')
    
# ref - s.102
def SequentialSearch(Array,x):
    '''
    For sequential search, we look sequentially at each element of the Array
    until we either come to the end of the array or find an item bigger
    than x. ARRAY MUST BE ORDERED IN INCREASING LENGTH.
    '''
    for i in range(len(Array)):
        if Array[i]>x:
            return Array[i-1]
    return Array[-1] # TO TEST

# ref - s.103
def BinSearch(Array,x,demonstrate=False):
    '''
    Look for x in ordered Array. Compare x to y in the middle of the
    array: If x < y, then search the first half of the array, otherwise
    search the second half of the array
    '''
    if len(Array) > 1: 
        half = int(round(len(Array)/2))
        if Array[:half][-1] >= x:
            if demonstrate:
                print(Array,'-->',Array[:half],' + ',Array[half:])
                print('LEFT',Array[:half],'\n')
            return BinSearch(Array[:half],x,True)
        else:
            if demonstrate:
                print(Array,'-->',Array[:half],' + ',Array[half:])
                print('RIGHT',Array[half:],'\n')
            return BinSearch(Array[half:],x,True)
    else:
        return Array[0]

# ref - s.105
def MergeSort(Array,demonstrate=False):
    
    if demonstrate:
        print('DIVIDE')
        print(Array)
    
    def conquer(a,b):
        ac = 0
        bc = 0
        lst =[]
        for i in range(len(a)+len(b)):
            if ac < len(a) and bc < len(b):
                if a[ac] <= b[bc]:
                    lst.append(a[ac])
                    ac += 1
                else:
                    lst.append(b[bc])
                    bc += 1
            else:
                if ac == len(a):
                    lst = lst + [i for i in b if i not in lst]
                else:
                    lst = lst + [i for i in a if i not in lst]
        return lst

    def divide(Array):
        #if len(Array) == 1: # I believe this is non-essential but I'll leave it here
            #return [Array]
        half = int(round(len(Array)/2))
        a = Array[:half]
        b = Array[half:] 
        return [a,b]

    a = divide(Array)
    
    if demonstrate:
        print(a)

    while len(a) != len(Array):
        for i in a:
            if len(i)==1:
                continue
            a = a + divide(i)
            a.remove(i)
            print(a)
    if demonstrate:
        print('& CONQUER')

    while len(a)!=1:
        x = a[0]
        y = a[1]
        a += [conquer(x,y)]
        a.remove(x)
        a.remove(y)
        if demonstrate:
            print(a)
            
    return a[0]

# ref - s.111
def QuickSort(Array):
    # easy conceptually but impossible when trying to program literally
    pass

# ref - s.132
def BC(n,k):
    '''
    BC = Binomial Coefficient
    The number of ways of picking k items from n items, calculated recursively.
    '''
    if k == 0 or k == n:
        return 1
    else:
        return BC(n-1,k-1) + BC(n-1,k)

# ref - s.137
def Floyd(Array):
    '''
    Calculate the length (cost,weight) of a shortest path between
    each pair of nodes.

    > For Floyd's algorithm, assume problem has optimal
    substructure:
        if j is on a shortest path from i to k, then a shortest path from
        i to j and a shortest path from j to k can be composed for a
        shortest path from i to k.

    Takes in an adjacency matrix with only direct paths and returns optimised adjacency matrix with intermediate
    paths taken into account.
    '''
    D = Array
    for k in range(len(Array)):
        for i in range(len(Array)):
            for j in range(len(Array)):
                D[i][j] = min(D[i][j],D[i][k] + D[k][j])
    return D

