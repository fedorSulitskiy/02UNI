# CHESS TIME
from IPython.display import display
from IPython.display import clear_output
import pandas as pd
#pd.options.mode.chained_assignment = None  # default='warn'

class chess_pieces():
    '''
    Chess class which dictates behaviour and general rules for pieces.
    '''
    def __init__(self):
        self.create_pieces_dict()
        self.attack_vectors = []

    def create_pieces_dict(self):
        '''
        Creates a dictionary of key 2 letter index str and corresponding unicode chess symbol str
        as well as the other way round with key unicode chess symbol str corresponding to 2 letter index str
        '''
        picons = [chr(9812 + x) for x in range(12)]
        pieces = ['wk','wq','wr','wb','wn','wp','bk','bq','br','bb','bn','bp']
        pieces_dict = {}
        for i in range(12):
            pieces_dict[pieces[i]] = picons[i]
        for i in range(12):
            pieces_dict[picons[i]] = pieces[i]
        
        self.p_dict = pieces_dict
    
    def piece(self, picon=None, empty=True):
        '''
        INPUT:  picon = either a 2 letter index or unicode chess symbol (str)
                empty = bool
        OUTPUT: returns corresponding unicode chess symbol or 2 letter index (str)
                if empty = True  =>  returns empty str
        '''
        if picon is not None:
            return self.p_dict[picon]
        if empty == True:
            return ' '
    
    def look_up(self, position, icon = False):
        rank = position[0]
        file = position[1]
        target = self.board.iloc[rank,file]
        if target == ' ':
            return False
        else:
            if icon:
                return self.p_dict[target]
            else:
                return True

    def create_mech_dct(self):
        '''
        Creates a dictionary which corresponds between the type of piece (str) and its mechanic function
        '''
        self.mech_dct = {'k':self.king, 'p':self.pawn, 'r':self.rook, 'b':self.bishop, 'n':self.knight, 'q':self.queen}

    def vector_of_movement(self,current_pos,y,z,colour):
        '''
        Determines available vectors of attack for one axis. Relevant to bishops, rooks and queen due to their
        long-range and linear attacks.
        '''
        attack_vectors = []
        i,j = current_pos
        for x in range(1,8):
            try:
                if i+x*y>=0 and j+x*z>=0:
                    if self.look_up((i+x*y,j+x*z)) == True:
                        if self.look_up((i+x*y,j+x*z), icon=True)[0]!=colour:
                            attack_vectors.append((i+x*y,j+x*z))
                            break
                        else:
                            break
                    attack_vectors.append((i+x*y,j+x*z))
                else:
                    continue
            except:
                break
        return attack_vectors

    def pawn(self, current_pos, colour):
        '''
        Pawns have very weird and particular mechanics, not least being directional...
        '''
        attack_vectors = []
        i,j = current_pos

        if colour == 'w':
            start,direction = 6,-1
        else:
            start,direction = 1,1
        
        if i == start: # LONG MARCH
            if self.look_up((i+2*direction,j)) == False:
                attack_vectors.append((i+2*direction,j))
        
        if self.look_up((i+direction,j)) == False: # SHORT DASH
            attack_vectors.append((i+direction,j))
        
        for x in [-1,1]: # double check
            try:
                if self.look_up((i+direction,j+x)) == False:
                    pass
                else:
                    if self.look_up((i+direction,j+x), True)[0] == colour:
                        pass
                    else:
                        attack_vectors.append((i+direction,j+x))
            except:
                continue
  
        self.attack_vectors = attack_vectors

    def bishop(self, current_pos, colour):
        attack_vectors = []

        attack_vectors.extend(self.vector_of_movement(current_pos,1,1,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,-1,-1,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,1,-1,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,-1,1,colour))

        self.attack_vectors = attack_vectors

    def rook(self, current_pos, colour):
        attack_vectors = []

        attack_vectors.extend(self.vector_of_movement(current_pos,0,1,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,0,-1,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,1,0,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,-1,0,colour))

        self.attack_vectors = attack_vectors
    
    def queen(self, current_pos, colour):
        attack_vectors = []

        ### BISHOP MECHANICS ###
        attack_vectors.extend(self.vector_of_movement(current_pos,1,1,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,-1,-1,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,1,-1,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,-1,1,colour))
        ###  ROOK MECHANICS  ###
        attack_vectors.extend(self.vector_of_movement(current_pos,0,1,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,0,-1,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,1,0,colour))
        attack_vectors.extend(self.vector_of_movement(current_pos,-1,0,colour))

        self.attack_vectors = attack_vectors

    def king(self, current_pos, colour):
        ### KING IS JUST DECREPIT QUEEN ###
        attack_vectors = []
        available_vectors = []
        i,j = current_pos
   
        for x in range(-1,2):
            available_vectors.append((i+x,j+x))
            available_vectors.append((i+x,j))
            available_vectors.append((i,j+x))
        for x in available_vectors:
            m,n=x    
            try:
                if m>=0 and n>=0:
                    if self.look_up(x) == True:
                        if self.look_up(x, icon=True)[0]!=colour:
                            attack_vectors.append(x)
                            continue
                        else:
                            continue
                    attack_vectors.append(x)
                else:
                    continue
            except:
                    continue
        self.attack_vectors = attack_vectors
        self.king_potential_moves = attack_vectors    

    def knight(self, current_pos, colour):
        attack_vectors = []
        indices = [-2,-1,1,2]
        x,y = current_pos
        
        for i in indices:
            for j in indices:
                if x+i>=0 and y+j>=0 and abs(i)!=abs(j):
                    try:
                        if self.look_up((x+i,y+j)) == True:
                            if self.look_up((x+i,y+j), icon=True)[0]!=colour:
                                attack_vectors.append((x+i,y+j))
                                continue
                            else:
                                continue
                        attack_vectors.append((x+i,y+j))
                    except:
                        continue
                else:
                    continue
        self.attack_vectors = attack_vectors

#====================================================================================#

class chess_game(chess_pieces):
    '''
    Chess class which dictates general and specific mechanics of running the game
    '''
    def __init__(self):
        chess_pieces.__init__(self)
        self.going_colour = 'w'
        self.selected_piece_loc = None
        self.king_in_danger = None
        self.castling_in_motion = False
        self.create_board()
        self.create_loc_dict()
        self.create_mech_dct()
        self.endgame = False
    
    def help(self):
        print('WELCOME TO FEDORS CHESS!!')
        print('=================================================================================================')
        self.create_board()
        self.populate_board()
        self.show_board()
        print('=================================================================================================')
        print('>Whites play first!')
        print(">To select your piece, type it's coordinates into the input")
        print(">The red squares will show available attack positions")
        print(">The blue square shows initial position of your selected piece")
        print(">Type the target's coordinates and press enter to make a move")
        print('>If you change your mind feel free to press enter without typing anything to deselct your piece')
        print(">To castle, type RIGHTCASTLING or LEFTCASTLING, blacks and whites share the same rights and lefts")
        
    def create_board(self):
        df = pd.DataFrame(({'chess': ['8','7','6','5','4','3','2','1'],
                                'A': [' ',' ',' ',' ',' ',' ',' ',' '],
                                'B': [' ',' ',' ',' ',' ',' ',' ',' '], 
                                'C': [' ',' ',' ',' ',' ',' ',' ',' '],
                                'D': [' ',' ',' ',' ',' ',' ',' ',' '],
                                'E': [' ',' ',' ',' ',' ',' ',' ',' '],
                                'F': [' ',' ',' ',' ',' ',' ',' ',' '],
                                'G': [' ',' ',' ',' ',' ',' ',' ',' '],
                                'H': [' ',' ',' ',' ',' ',' ',' ',' '],})).set_index('chess')
        self.board = df

    def show_board(self):
        def style_cells(x):
            color = 'background-color: grey'
            df1 = pd.DataFrame('', index=x.index, columns=x.columns)
            for i in range(0,8,2):
                for j in range(1,8,2):
                    df1.iloc[i,j] = color
            for i in range(1,8,2):
                for j in range(0,8,2):
                    df1.iloc[i,j] = color
            if self.selected_piece_loc != None:
                df1.iloc[self.selected_piece_loc[0],self.selected_piece_loc[1]] = 'background-color: cornflowerblue'
            for i,j in self.attack_vectors:
                df1.iloc[i,j] = 'background-color: salmon'
            return df1

        mask = self.board.style.apply(style_cells, axis=None)
        display(mask)
    
    def populate_board(self):
        self.board.iloc[6]    = self.piece('wp',empty=False)
        self.board.iloc[7,0] = self.piece('wr',empty=False)
        self.board.iloc[7,7] = self.piece('wr',empty=False)
        self.board.iloc[7,1] = self.piece('wn',empty=False)
        self.board.iloc[7,6] = self.piece('wn',empty=False)
        self.board.iloc[7,2] = self.piece('wb',empty=False)
        self.board.iloc[7,5] = self.piece('wb',empty=False)
        self.board.iloc[7,4] = self.piece('wk',empty=False)
        self.board.iloc[7,3] = self.piece('wq',empty=False)
        self.board.iloc[1]    = self.piece('bp',empty=False)
        self.board.iloc[0,0] = self.piece('br',empty=False)
        self.board.iloc[0,7] = self.piece('br',empty=False)
        self.board.iloc[0,1] = self.piece('bn',empty=False)
        self.board.iloc[0,6] = self.piece('bn',empty=False)
        self.board.iloc[0,2] = self.piece('bb',empty=False)
        self.board.iloc[0,5] = self.piece('bb',empty=False)
        self.board.iloc[0,4] = self.piece('bk',empty=False)
        self.board.iloc[0,3] = self.piece('bq',empty=False)

    def create_loc_dict(self):
        '''
        Creates dictionary which corresponds chess coordinates to python coordinates
        '''
        self.letters = ['A','B','C','D','E','F','G','H']
        numbers = [i for i in range(1,9)]
        locations = []
        for i in list(reversed(numbers)):
            for j in self.letters:
                locations.append(j+str(i))

        indices = []
        for i in range(8):
            for j in range(8):
                indices.append((i,j))

        locations_dict = {}
        for i in range(64):
                locations_dict[locations[i]] = indices[i]
        self.loc_dict = locations_dict

    def select_cell(self):
        '''
        INPUT:  user input of location of chess cell you like
        OUTPUT: returns the kind of piece it is, as 2 letter index as str
        '''
        while True:
            select = input('Select you piece: ')
            if 'CASTLING' in select:
                if self.castling(select):
                    self.castling_in_motion = False
                    break
                else:
                    self.castling_in_motion = False
                    print('Your move is invalid')
                    continue
            elif select in self.loc_dict:
                rank = self.loc_dict[select][0]
                file = self.loc_dict[select][1]
                picon = self.board.iloc[rank,file]
                if picon == ' ':
                    print('Your selection is invalid')
                else:
                    self.selected_piece_loc = (rank,file)
                    self.piece_in_motion = self.piece(picon=picon, empty=False)
                    if self.going_colour == 'w':
                        if self.piece_in_motion[0] == 'w':
                            self.mech_dct[self.piece_in_motion[1]](self.selected_piece_loc, self.piece_in_motion[0])
                            self.show_board()
                            self.move_your_piece()
                            break
                        else:
                            print('Your selection is invalid')
                    else:
                        if self.piece_in_motion[0] == 'b':
                            self.mech_dct[self.piece_in_motion[1]](self.selected_piece_loc, self.piece_in_motion[0])
                            self.show_board()
                            self.move_your_piece()
                            break
                        else:
                            print('Your selection is invalid')
            else:
                continue

    def check_possibility_of_move(self, target_loc):
        if target_loc in self.attack_vectors:
            return True
        else:
            return False

    def move_your_piece(self):
        while True and self.castling_in_motion == False:
            select = input('Select you move: ')
            if select == '':
                self.select_cell()
                break
            rank = self.loc_dict[select][0]
            file = self.loc_dict[select][1]
            if self.check_possibility_of_move((rank,file)) == False:
                print('Your move is invalid')
            else:
                self.board.iloc[rank,file] = self.piece(picon=self.piece_in_motion, empty=False)
                self.board.iloc[self.selected_piece_loc[0],self.selected_piece_loc[1]] = self.piece()
                self.attack_vectors = []
                self.show_board()
                break

    def castling(self, direction):

        def execute(rank,kfile,rn_file,ro_file):
            self.board.iloc[rank,kfile] = self.piece(picon=self.going_colour+'k', empty=False)
            self.board.iloc[rank,4] = self.piece()
            self.board.iloc[rank,rn_file] = self.piece(picon=self.going_colour+'r', empty=False)
            self.board.iloc[rank,ro_file] = self.piece()

        self.castling_in_motion = True
        if self.going_colour == 'w':
            axis = 7
        else:
            axis = 0
        
        if direction[0] == 'R':
            kfile = 6
            rn_file = 5
            ro_file = 7
            if True in [self.look_up((axis, x+4)) for x in range(1,3)]:
                return False
            else:
                execute(axis,kfile,rn_file,ro_file)
                return True
        elif direction[0] == 'L':
            kfile = 2
            rn_file = 3
            ro_file = 0
            if True in [self.look_up((4-x, axis)) for x in range(1,4)]:
                return False
            else:
                execute(axis,kfile,rn_file,ro_file)
                return True
    
    def check_mate(self):
        self.king(self.where_is_king(self.going_colour),self.going_colour)
        potential_moves = self.king_potential_moves
        if self.king_in_danger == True:
            self.king_in_danger = False
            for i in potential_moves:
                self.check(king_pos = i)
                if self.king_in_danger == True:
                    print(self.going_colour+'lost!!!')
                    self.endgame = True      
        
    def where_is_king(self,colour):
        for i in self.letters:
            a = self.board[self.board[i]==self.piece([colour+'k'][0],empty=False)].index.values
            if len(a) != 0:
                king = i+a[0]
        return self.loc_dict[king]
    
    def vector_of_threat(self,current_pos,y,z,colour):
        '''
        Determines if a cell is under threat from an objects in the direction of a single axis.
        Doesn't determine if threat is real
        '''
        threats = []
        i,j = current_pos
        for x in range(1,8):
            try:
                if i+x*y>=0 and j+x*z>=0:
                    if self.look_up((i+x*y,j+x*z)) == True:
                        if self.look_up((i+x*y,j+x*z), icon=True)[0]!=colour:
                            threats.append((i+x*y,j+x*z,self.look_up((i+x*y,j+x*z), icon=True)))
                            break
                        else:
                            break
                else:
                    continue
            except:
                break
        self.threats = threats
        return threats

    def check(self, king_pos = None):
        
        threats = []
        for col in ['w','b']:
            if king_pos == None:
                king = self.where_is_king(col)
            else:
                king = king_pos
                col = self.going_colour
            # check threats from queen, bishop or pawns
            threats.extend(self.vector_of_threat(king,1,1,col))
            threats.extend(self.vector_of_threat(king,-1,-1,col))
            threats.extend(self.vector_of_threat(king,1,-1,col))
            threats.extend(self.vector_of_threat(king,-1,1,col))
            if len(threats) != 0:
                for i,j,k in threats:
                    if k[1] == 'q' or k[1] == 'b':
                        self.king_in_danger = True
                    elif k[1] == 'p' and abs(i-king[0])==1 and abs(j-king[1])==1:
                        self.king_in_danger = True
                threats = []
            threats.extend(self.vector_of_threat(king,0,1,col))
            threats.extend(self.vector_of_threat(king,0,-1,col))
            threats.extend(self.vector_of_threat(king,1,0,col))
            threats.extend(self.vector_of_threat(king,-1,0,col))
            if len(threats) != 0:
                for i,j,k in threats:
                    if k[1] == 'q' or k[1] == 'r':
                        self.king_in_danger = True
                threats = []      
            # check knight threats
            indices = [-2,-1,1,2]
            x,y = king
            for i in indices:
                for j in indices:
                    if x+i>=0 and y+j>=0 and abs(i)!=abs(j):
                        try:
                            if self.look_up((x+i,y+j)) == True:
                                if self.look_up((x+i,y+j), icon=True)[0]!=col:
                                    threats.append((x+i,y+j,self.look_up((x+i,y+j), icon=True)))
                                    continue
                                else:
                                    continue
                        except:
                            continue
                    else:
                        continue
            if len(threats) != 0:
                for i,j,k in threats:
                    if k == 'n':
                        self.king_in_danger = True
            threats = []

            if self.king_in_danger:
                print('CHECK!!!')

    def queening(self):
        '''
        Allows you to choose what ever piece you want once a pawn reaches the other side of the board
        '''
        for col in ['w','b']:
            for i in range(8):
                try:
                    if col == 'w':
                        axis = 0
                    else:
                        axis = 7
                    if self.look_up((axis,i),True) == col+'p':
                        print('You can turn your pawn into another piece!')
                        print('==========================================')
                        print('>Type either of n/b/r/q for knight/bishop/rook or queen to select your new piece')
                        piece_you_want = input('Please select which piece you would like: ')
                        self.board.iloc[axis,i] = self.piece(picon=col+piece_you_want, empty=False)
                except:
                    continue
                
#====================================================================================#

def game():
    '''
    Method which runs the game
    '''
    chess = chess_game()
    chess.help()
    while chess.endgame == False:
        chess.select_cell()
        chess.check()
        chess.check_mate()
        chess.queening()
        clear_output(wait=True)
        if chess.going_colour == 'w':
            print('Blacks turn')
            chess.attack_vectors = []
            chess.show_board()
            chess.going_colour = 'b'
        elif chess.going_colour == 'b':
            print('Whites turn')
            chess.attack_vectors = []
            chess.show_board()
            chess.going_colour = 'w'