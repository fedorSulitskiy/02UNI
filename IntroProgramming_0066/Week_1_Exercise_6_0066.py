# A
def sorter(a, b, c):
    '''
    Takes input of three integers in any order and prints
    said integers in descending order

    Parameters:
    ===========
    a - input integer
    b - input integer
    c - input integer
    '''
    x = 0
    y = 0
    z = 0
    lst = [a, b, c]
    switch = True
    while switch:
        if len(lst) == 3:
            for i in range(3):
                if lst[i] > lst[i - 1] and lst[i] > lst[i - 2]:     # find largest number in input sequence
                    x = lst[i]
                    lst.pop(i)
                    break
                elif lst[i] == lst[i - 1] or lst[i] == lst[i - 2]:  # check for duplicates
                    x = lst[i]
                    lst.pop(i)
                    break
        elif len(lst) == 2:
            for i in range(2):
                if lst[i] > lst[i - 1]:         # find second largest number in input sequence
                    y = lst[i]
                    lst.pop(i)
                    break
                elif lst[i] == lst[i - 1]:      # check for duplicates
                    y = lst[i]
                    lst.pop(i)
                    break
        else:       # assign the remaining, smallest number
            z = lst[0]
            switch = False

    print(x, y, z)

# B
def verify_password(password):
    '''
    Compares the input password(directly into the function) with the
    password input by the user when the method is run

    Parameters:
    ===========
    password - string variable, sets the password
    '''
    if input('Please input your password: ') == password:
        print('Password accepted!')
    else:
        print('Wrong password')

# C
def ucl_grade():
    '''
    Takes input of student's module mark and returns corresponding grade

    Parameters:
    ===========
    mark - student's average module mark, integer
    '''
    mark = int(input('Please submit your average module mark: '))
    if mark > 100 or mark < 0:
        print('Please input a possible grade (0-100)')
    elif mark > 69:
        print('Distinction')
    elif mark < 50:
        print('Fail')
    else:
        print('Pass')