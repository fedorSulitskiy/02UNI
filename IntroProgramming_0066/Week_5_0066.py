# 3 
def targetSum(nums, target):
    '''
    Method takes in a list of integers and returns lists of 4 elements
    that add up to the target. The output list consists of the elements
    present in the input list.
    
    Parameters:
        nums  (list): list of integers
        target (int): integer
        
    Returns:
        l (list of lists): list of lists that each contains 4 elements
                           that each add up to target
    '''
    def permutation(lst): # alternatively library intertools can be used
        if len(lst) == 0: # import itertools
                          # perm = list(itertools.permutations(nums))
            return []     # this is a lot easier
        if len(lst) == 1:
            return [lst]
        l = [] 

        for i in range(len(lst)):
            m = lst[i]
            remLst = lst[:i] + lst[i+1:]
            for p in permutation(remLst):
                l.append([m] + p)
        return l
    perm = permutation(nums)
    l = []
    for i in perm:
        j = i[:4]
        if sum(j) == target:
            j.sort()
            if j not in l:
                l.append(j)          
    return l

# 4
