# 3
def exercise_3(x):
    import math
    return 'f(x)=',round(math.cos(2*x),3),"f'(x)=", round(math.sin(2*x)*-2,3),"f''(x)=",round(-4*math.cos(2*x),3)

# 4
def exercise_4():
    pass

# 5
def accept_login(users, username, password):
    if username in users.keys():
        if users[username] == password:
            return True
        else:
            return False
    else:
        return False
    
# 6
def exercise_6(x):
    import math
    units = ("B", "KB", "MB", "GB")
    for i in range(0,31,10):
        print(round(x/math.pow(2,i),1), units[int(i/10)])