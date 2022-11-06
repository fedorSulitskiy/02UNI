# 1
def exercise_1():
    '''
    > outputs all numbers between 2000 and 4000	
    that are divisible by 9 but aren't multiples of 2
    '''
    for i in range(2000,4001):
        if i%9==0 and i%2!=0:
            print(i)
            
# 2
def exercise_2(X=70,H=25):
    '''
    > takes in any number of y (int) variables as user inputs
    > prints a series of solutions to the equation from the original exercise,
    rounded to 1 significant figure
    ==============================
    to finish y inputs press enter
    '''
    y = []
    while True:
        user_input = input('Enter your Y values: ')
        if user_input == '':
            break
        y.append(int(user_input))
    
    for Y in y:
        print(round(((3*X*Y)/H)**0.5), end = " ")
        
# 3
def exercise_3(lst):
    '''
    > Sorts the input list of tuples of format (name(str),age(int),score(int))
    by the following priority : name > age > score
    '''
    import operator
    print(sorted(lst, key = operator.itemgetter(0,1,2)))
    
# 4
def exercise_4(lstA,lstB):
    '''
    > takes 2 lists of integers as inputs
    > returns list of elements common to both input lists
    '''
    lstA = set(lstA)
    lstB = set(lstB)
    lstC = []
    for i in lstA:
        for j in lstB:
            if i == j:
                lstC.append(i)
    print(lstC)
    
# 5 
def exercise_5(str):
    '''
    > takes string as input
    > returns if the input string is a palindrome or not 
    '''
    if len(str) % 2 == 0:
        if str[:int(len(str)/2)] == str[:int(len(str)/2)-1:-1]:
            print('yes, its a palindrome')
        else:
            print('no, its not a palindrome')
    else:
        str=str.replace(str[round(len(str)/2)],'')
        if str[:int(len(str)/2)] == str[:int(len(str)/2)-1:-1]:
            print('yes, its a palindrome')
        else:
            print('no, its not a palindrome')
            
# 6
def exercise_6(lst):
    '''
    > takes list of string as input
    > return a list of tuples of format (str, number of repeated occurances) where the list contains top 4 most repeated words
    '''
    import operator
    ret = []
    for i in lst:
        ret.append((i,lst.count(i)))
    ret = set(ret)
    print(sorted(list(ret), key = operator.itemgetter(1))[:2:-1])
    
# 7 TIK TAK TOE
class TikTakToe():
    '''
    Class required to play the game
    '''
    def __init__(self):
        self.spot = [' ',' ',' ',
                     ' ',' ',' ',
                     ' ',' ',' ']
        self.player_sign = None
        self.comp_sign = None
        self.first = None
        self.computerWon = False
        self.playerWon = False
        self.tie = None
        pass 
    
    def show_battlefield(self):
        print(f' {self.spot[6]} | {self.spot[7]} | {self.spot[8]} ')
        print('-----------')
        print(f' {self.spot[3]} | {self.spot[4]} | {self.spot[5]} ')
        print('-----------')
        print(f' {self.spot[0]} | {self.spot[1]} | {self.spot[2]} ')
        print('=================================','\n')
    
    def demonstrate_controls(self):
        print('GAME TUTORIAL', '\n')
        self.spot = ['1','2','3',
                     '4','5','6',
                     '7','8','9'] 
        print('FOR PLAYER TO PLAY USE DIALS TO SELECT SIGN LOCATION')
        print('====================================================')
        self.show_battlefield()
        self.spot = [' ',' ',' ',
                     ' ',' ',' ',
                     ' ',' ',' ']
        
    def choose_sign(self):
        while True:
            sign = input("Choose your fighter insignia (X/O): ")
            print('\n')
            if sign == 'X':
                print('Player is [X] and computer is [O]')
                print('=================================')
                print('Player Goes first!')
                self.first = True
                self.player_sign = 'X'
                self.comp_sign = 'O'
                break
            elif sign == 'O':
                print('Player is [O] and computer is [X]')
                print('=================================')
                print('Computer goes first!')
                print('=================================','\n')
                self.first = False
                self.player_sign = 'O'
                self.comp_sign = 'X'
                break
            else:
                print('Please select a valid symbol (X/O): ')
        
    def player_goes(self):
        while True:
            position = input('Make your move! (1-9) ')
            if position.isnumeric():
                position = int(position)
                if position - 1 not in self.where_empty():
                    print('Please input a valid index!')
                elif position > 9:
                    print('Please input a valid index!')
                else:
                    self.spot[position-1] = self.player_sign
                    break
            else:
                print('Please input a valid index!')
                
    def where_empty(self):
        lst = []
        for indx, i in enumerate(self.spot):
            if i == ' ':
                lst.append(indx)
        return lst
    
    def computer_brains(self):
        '''
        Leave it as separate method in case I figure out an elegant way of making computer make smart moves
        '''
        import random
        empty = self.where_empty()
        random_pos = random.choice(empty)
        return random_pos
    
    def computer_goes(self, position):
        self.spot[position] = self.comp_sign
    
    def did_i_win(self,turn):
        if turn == 'comp':
            sign = self.comp_sign
        else:
            sign = self.player_sign
        lr = self.spot[0] == sign and self.spot[1] == sign and self.spot[2] == sign # low row
        mr = self.spot[3] == sign and self.spot[4] == sign and self.spot[5] == sign # mid row
        tr = self.spot[6] == sign and self.spot[7] == sign and self.spot[8] == sign # top row
        lc = self.spot[0] == sign and self.spot[3] == sign and self.spot[6] == sign # left column
        mc = self.spot[1] == sign and self.spot[4] == sign and self.spot[7] == sign # mid column
        rc = self.spot[2] == sign and self.spot[5] == sign and self.spot[8] == sign # right column
        td = self.spot[0] == sign and self.spot[4] == sign and self.spot[8] == sign # top diagonal (bottom left corner to top right)
        bt = self.spot[6] == sign and self.spot[4] == sign and self.spot[2] == sign # bottom diagonal (top left corner to bottom right)
        if lr or mr or tr or lc or mc or rc or td or bt:
            if turn == 'comp':
                self.computerWon = True
                print('COMPUTER WON!!!!')
            else:
                self.playerWon = True
                print('PLAYER WON!!!!')
    
    def is_it_tie(self):
        empty = self.where_empty()
        if len(empty) == 0:
            if self.computerWon == False and self.playerWon == False:
                print('ITS A TIE')
            self.tie = True

# code to play the game
           
ttt = TikTakToe()
ttt.demonstrate_controls()
ttt.choose_sign()
stop = True
first_turn = ttt.player_sign

def player_turn(turn):
    ttt.player_goes()
    ttt.show_battlefield()
    ttt.did_i_win(turn)
    ttt.is_it_tie()
    
def computer_turn(turn):
    print('Computer move!')
    pos = ttt.computer_brains()
    ttt.computer_goes(pos)
    ttt.show_battlefield()
    ttt.did_i_win(turn)
    ttt.is_it_tie()
    
while stop == True:
    if first_turn == 'X':
        player_turn('player')
        if ttt.playerWon == True:
            break
        elif ttt.tie == True:
            break
    else:
        computer_turn('comp')
        if ttt.computerWon == True:
            break
        elif ttt.tie == True:
            break
            
        player_turn('player')
        if ttt.playerWon == True:
            break
        elif ttt.tie == True:
            break
        
    first_turn = "It's over." 
    computer_turn('comp')
    if ttt.computerWon == True:
        break
    elif ttt.tie == True:
        break
        
    player_turn('player')
    if ttt.playerWon == True:
        break
    elif ttt.tie == True:
        break