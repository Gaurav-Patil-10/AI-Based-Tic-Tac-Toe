import math

import time


import random
import string

s1 = string.ascii_lowercase

main_list = ["_"] * 9


''' 0 1 2
    3 4 5
    6 7 8'''

'''(1, 3) (2, 3) (3, 3)
(1, 2) (2, 2) (3, 2)
(1, 1) (2, 1) (3, 1)'''

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input('Enter the coordinates: ').split(" ")
            l1 = [[1,3],[2,3],[3,3],[1,2],[2,2],[3,2],[1,1],[2,1],[3,1]]
            val = 0
            for x in l1:
                if x[0] == int(square[0]) and x[1] == int(square[1]):
                    val = l1.index(x)
            try:
                # val = int()
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("This cell is occupied! Choose another one!")
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        print(f'''---------
| {self.board[0]} {self.board[1]} {self.board[2]} |
| {self.board[3]} {self.board[4]} {self.board[5]} |
| {self.board[6]} {self.board[7]} {self.board[8]} |
---------''')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    # if print_game:
    #     game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                # print(letter + ' makes a move to square {}'.format(square))
                
                
                print('Making move level "hard"')
                game.print_board()

                
                # print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player
            

        # time.sleep(.8)

    if print_game:
        print('Draw')





def diag__ (list_1):

    global main_list

    l1 = list(list_1)

    diagonal_1 = [0 , 4 , 8]
    diagonal_2 = [2 ,4 ,6]

    for x in l1:
        if x not in list(diagonal_1 + diagonal_2):
            l1.remove(x)

    # print(l1)

    move = list(diagonal_1)
    move_2 = list(diagonal_2)
    
    for x in l1:
        if x in move:  
            move.remove(x)
        if x in move_2: 
            move_2.remove(x)

    # print(move , move_2)
    if len(move) == 1:
        if main_list[move[0]] == "_":
            return move[0]
        
    elif len(move_2) == 1:
        if main_list[move_2[0]] == "_":
            return move_2[0]

       
    
def hori__(list1):

    hor_1 = [0 , 1 , 2]
    hor_2 = [3 ,4 , 5]
    hor_3 = [6, 7, 8 ]

    move = list(hor_1)
    move_2 = list(hor_2)
    move_3 = list(hor_3)
    
    for x in list1:
        if x in move:  
            move.remove(x)
        if x in move_2: 
            move_2.remove(x)
        if x in move_3:
            move_3.remove(x)

    # print(move , move_2 , move_3)



    if len(move) == 1:
        if main_list[move[0]] == "_":
            return move[0]
        
    elif len(move_2) == 1:
        if main_list[move_2[0]] == "_":
            return move_2[0]

    elif len(move_3) == 1:
        if main_list[move_3[0]] == "_":
            return move_3[0]

    
def ver__(list1):
    hor_1 = [0 , 3 , 6]
    hor_2 = [1 ,4 , 7]
    hor_3 = [2, 5, 8 ]

    move = list(hor_1)
    move_2 = list(hor_2)
    move_3 = list(hor_3)
    
    for x in list1:
        if x in move:  
            move.remove(x)
        if x in move_2: 
            move_2.remove(x)
        if x in move_3:
            move_3.remove(x)

    # print(move , move_2 , move_3)



    if len(move) == 1:
        if main_list[move[0]] == "_":
            return move[0]
        
    elif len(move_2) == 1:
        if main_list[move_2[0]] == "_":
            return move_2[0]

    elif len(move_3) == 1:
        if main_list[move_3[0]] == "_":
            return move_3[0]

    


def move_(x1):
    global main_list

    index_list = []
    for x in range(len(main_list)):
        if main_list[x] == x1:
            index_list.append(x)
            
    ans = hori__(index_list)
    ans1 = diag__(index_list)
    ans2 = ver__(index_list)
    if ans == None:
        if ans2 == None:
            return ans1
        else:
            return ans2
    else:
        return ans
    


# print(move_("X"))



def user_co_ordinates(x , y):

    '''function for co ordinates manipulation'''

    l1 = [[1,3],[2,3],[3,3],[1,2],[2,2],[3,2],[1,1],[2,1],[3,1]]
    for c in l1:
        if x == c[0] and y == c[1]:
            return l1.index(c)






def check():

    ''' function for checking the horizontal , vertical and diagonals'''
    global main_list 

    count_ = 0

    for x in main_list:
        if x == "_":
            count_ += 1

    if count_ == 0:
        return "Draw"

    else:
        ans1 = horizontal(main_list)
        if ans1 == False:
            ans2 = vertical(main_list)
            if ans2 == False:
                ans3 = diagonal(main_list)
                if ans3 == False:
                    return False
                else:
                    if ans3 != "_":
                        return ans3
                    else:
                        return False
            else:
                if ans2 != "_":
                        return ans2
                else:
                    return False
        else:
            if ans1 != "_":
                        return ans1
            else:
                return ans1

def horizontal(main_):

    '''checking for horizontal'''

    a = set([main_[x] for x in range(0, 3)])
    b = set([main_[x] for x in range(3, 6)])
    c = set([main_[x] for x in range(6, 9)])

    a = list(a)
    b = list(b)
    c = list(c)
    # print(a, b, c)
    if len(a) == 1:
        if a[0] != "_" or a[0] != None:
            return a[0]
       
    elif len(b) == 1 :
        if b[0] != "_" or b[0] != None :
            return b[0]
    elif len(c) == 1:
        if c[0] != "_" or c[0] != None:
            return c[0]

    else:
        return False

def vertical (main_):
    '''checking for the vertical '''
    a = set([main_[x] for x in range(0, 7, 3)])
    b = set([main_[x] for x in range(1, 8, 3)])
    c = set([main_[x] for x in range(2, 9, 3)])

    a = list(a)
    b = list(b)
    c = list(c)
    # print(a,b,c)
    if len(a) == 1:
        if a[0] != "_" or a[0] != None:
            return a[0]
    elif len(b) == 1:
        if b[0] != "_" or b[0] != None:
            return b[0]
    elif len(c) == 1:
        if b[0] != "_" or c[0] != None:
            return b[0]

    else:
        return False

def diagonal(main_):

    '''checking for the diagonal elements'''

    a = set([main_[x] for x in range(0, 9, 4)])
    b = set([main_[x] for x in range(2, 7, 2)])

    a = list(a)
    b = list(b)
    # print(a,b)
    if len(a) == 1:
        if a[0] != "_" or a[0] != None:
            return a[0]
    elif len(b) == 1:
        if b[0] != "_" or b[0] != None:
            return b[0]
    else:
        return False


def user_input():

    '''function for handling the user input'''

    km = 1
    while km == 1:
        in__ = input('Enter the coordinates: ')
        if in__[0] in s1:
            print("You should enter numbers!")
        else:
            nums = in__.split(" ")
            num_1 = int(nums[0])
            num_2 = int(nums[1])
            co_ = user_co_ordinates(num_1, num_2)

            if num_1 > 3 or num_1 <= 0 or num_2 <= 0 or num_2 > 3:
                print("Coordinates should be from 1 to 3!")
                continue
            if main_list[co_] != "_":
                print("This cell is occupied! Choose another one!")
                continue

            else:
                return co_

def user_vs_user():
    global main_list
    main = 5
    while main == 5:
        co = user_input()
        if main_list[co] != "_":
            m = 5
            
        else:
            main_list[co] = "X"
        # print('Making move level "easy"')
        
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        

        ans = check()

        if ans != False:
            if ans != None:
                if  ans != "_":
                    if ans == "Draw":
                        print(f"{ans}")
                        main = 4
                        return True
                    else:
                        print(f"{ans} wins")
                        main = 4
                        return True
                        
                        
        else:
            main = 5

        
        co1 = user_input()
        if main_list[co1] != "_":
            
            pass
        else:
            main_list[co1] = "O"
        # print('Making move level "easy"')
        
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        
        ans = check()

        if ans != False:
            if ans != None:
                if  ans != "_":
                    if ans == "Draw":
                        print(f"{ans}")
                        main = 5
                        return True
                    else:
                        print(f"{ans} wins")
                        return True
        else:
            main = 5



def com_vs_user( level = 0):
    global main_list
    main = 5
    while main == 5:
        if level == 2:
            co = move_("X")
            level_name = "medium"

        elif level == 4:
            co = move_("X")
            level_name = "hard"

        else:
            co = random.randint(0 , 8)
            level_name = "easy"
        if co == None or main_list[co] != "_":
            m = 5
            while m == 5:
                co_1 = random.randint(0 , 8)
                if main_list[co_1] != "_":
                    m = 5
                else:
                    main_list[co_1] = "O"
                    m = 4
        else:
            main_list[co] = "X"
        print(f'Making move level "{level_name}"')
        
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        

        ans = check()

        if ans != False:
            if ans != None:
                if  ans != "_":
                    if ans == "Draw":
                        print(f"{ans}")
                        main = 4
                        return True
                    else:
                        print(f"{ans} wins")
                        main = 4
                        return True
                        
                        
        else:
            main = 5

        
        co1 = user_input()
        if main_list[co1] != "_":
            # m = 5
            # while m == 5:
            #     co_1 = user_input()
            #     if main_list[co_1] != "_":
            #         m = 5
            #     else:
            #         main_list[co_1] = "O"
            #         m = 4
            pass
        else:
            main_list[co1] = "O"
        # print('Making move level "easy"')
        
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        
        ans = check()

        if ans != False:
            if ans != None:
                if  ans != "_":
                    if ans == "Draw":
                        print(f"{ans}")
                        main = 5
                        return True
                    else:
                        print(f"{ans} wins")
                        return True
        else:
            main = 5





def com_vs_com(level = 0):
    global main_list
    main = 5
    while main == 5:
        if level == 2:
            co = move_("O")
            level_name = "medium"
        elif level == 4:
            co = move_("O")
            level_name = "hard"
        elif level == 5:
            co = move_("O")
            level_name = "hard"
        elif level == 6:
            co = move_("O")
            level_name = "easy"
        elif level == 7:
            co = move_("O")
            level_name = "hard"
        
        

        else:
            co = random.randint(0 , 8)
            level_name = "easy"
        if co == None or main_list[co] != "_":
            m = 5
            while m == 5:
                co_1 = random.randint(0 , 8)
                if main_list[co_1] != "_":
                    m = 5
                else:
                    main_list[co_1] = "X"
                    m = 4
        else:
            main_list[co] = "X"
        print(f'Making move level "{level_name}"')
        
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        

        ans = check()

        if ans != False:
            if ans != None:
                if  ans != "_":
                    if ans == "Draw":
                        print(f"{ans}")
                        main = 4
                        return True
                    else:
                        print(f"{ans} wins")
                        main = 4
                        return True
                        
                        
        else:
            main = 5

        
        if level == 2:
            co1 = move_("X")
            level_name = "medium"
        elif level == 4:
            co1 = move_("X")
            level_name = "hard"

        elif level == 5:
            co1 = move_("X")
            level_name = "medium"

        elif level == 6:
            co1 = move_("X")
            level_name = "hard"
        elif level == 7:
            co1 = move_("X")
            level_name = "easy"

        else:
            co1 = random.randint(0 , 8)
            level_name = "easy"
        if co1 == None or main_list[co1] != "_":
            m = 5
            while m == 5:
                co_1 = random.randint(0 , 8)
                if main_list[co_1] != "_":
                    m = 5
                else:
                    main_list[co_1] = "O"
                    m = 4
        else:
            main_list[co1] = "O"
        print(f'Making move level "{level_name}"')
        
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        
        ans = check()

        if ans != False:
            if ans != None:
                if  ans != "_":
                    if ans == "Draw":
                        print(f"{ans}")
                        main = 5
                        return True
                    else:
                        print(f"{ans} wins")
                        return True
        else:
            main = 5


def user_vs_com(level = 0):

    global main_list
    main = 5
    while main == 5:
        co = user_input()
        if main_list[co] != "_":
            m = 5
            
        else:
            main_list[co] = "X"
        # print('Making move level "easy"')
        
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        

        ans = check()

        if ans != False:
            if ans != None:
                if  ans != "_":
                    if ans == "Draw":
                        print(f"{ans}")
                        main = 4
                        return True
                    else:
                        print(f"{ans} wins")
                        main = 4
                        return True
                        
                        
        else:
            main = 5


        if level == 2:
            co1 = move_("X")
            level_name = "medium"
        elif level == 4:
            co1 = move_("X")
            
            level_name = "hard"
        else:
            co1 = random.randint(0 , 8)
            level_name = "easy"
        if co1 == None:
            m = 5
            while m == 5:
                co_1 = random.randint(0 , 8)
                if main_list[co_1] != "_":
                    m = 5
                else:
                    main_list[co_1] = "O"
                    m = 4
        else:
            main_list[co1] = "O"
        print(f'Making move level "{level_name}"')
        
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        
        ans = check()

        if ans != False:
            if ans != None:
                if  ans != "_":
                    if ans == "Draw":
                        print(f"{ans}")
                        main = 5
                        return True
                    else:
                        print(f"{ans} wins")
                        main = 5
                        return True
        else:
            main = 5


def user_vs_medium():

    global main_list
    main = 5
    while main == 5:
        co = user_input()
        if main_list[co] != "_":
            m = 5
            
        else:
            main_list[co] = "X"
        # print('Making move level "easy"')
        
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        

        ans = check()

        if ans != False:
            if ans != None:
                if  ans != "_":
                    if ans == "Draw":
                        print(f"{ans}")
                        main = 4
                        return True
                    else:
                        print(f"{ans} wins")
                        main = 4
                        return True
                        
                        
        else:
            main = 5

        co1 = move_("X")
        if co1 == None:
            m = 5
            while m == 5:
                co_1 = random.randint(0 , 8)
                if main_list[co_1] != "_":
                    m = 5
                else:
                    main_list[co_1] = "O"
                    m = 4
        else:
            main_list[co1] = "O"
        print('Making move level "medium"')
        
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        
        ans = check()

        if ans != False:
            if ans != None:
                if  ans != "_":
                    if ans == "Draw":
                        print(f"{ans}")
                        main = 5
                        return True
                    else:
                        print(f"{ans} wins")
                        return True
        else:
            main = 5


    




k = 1
while k == 1:
    command = input("Input command: ")

    if command == "exit":
        exit()

    else:
        try:
            com = command.split(" ")
            if len(com) == 3:
                k = 2

            else:
                print("Bad parameters!")
                

        except Exception as e:
            print("Bad parameters!")

    if com[1] == "easy" and com[2] == "easy":
        main_list = ["_"] * 9
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = com_vs_com()
        if ans == True:
            k = 1

    elif com[1] == "easy" and com[2] == "user":
        main_list = ["_"] * 9
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = com_vs_user()
        if ans == True:
            k = 1

    elif com[1] == "user" and com[2] == "user":
        main_list = ["_"] * 9
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = user_vs_user()
        if ans == True:
            k = 1

    elif com[1] == "user" and com[2] == "easy":
        main_list = ["_"] * 9
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = user_vs_com()
        if ans == True:
            k = 1

    elif com[1] == "user" and com[2] == "medium":
        main_list = ["_"] * 9
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = user_vs_medium()
        if ans == True:
            k = 1
    elif com[1] == "medium" and com[2] == "user":
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = com_vs_user(level = 2)
        if ans == True:
            k = 1

    elif com[1] == "medium" and com[1] == "medium":
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = com_vs_com(level = 2)
        if ans == True:
            k = 1

    elif com[1] == "easy" and com[2] == "medium":
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = com_vs_com(level = 3)
        if ans == True:
            k = 1

    elif com[1] == "hard" and com[2] == "user":
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = com_vs_user(level = 4)
        if ans == True:
            k = 1
    elif com[1] == "user" and com[2] == "hard":
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = user_vs_com(level = 4)
        if ans == True:
            k = 1
    elif com[1] == "hard" and com[2] == "hard":
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = com_vs_com(level = 4)
        if ans == True:
            k = 1

    elif com[1] == "hard" and com[2] == "medium":
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = com_vs_com(level = 5)
        if ans == True:
            k = 1

    elif com[1] == "easy" and com[2] == "hard":
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = com_vs_com(level = 6)
        if ans == True:
            k = 1

    elif com[1] == "hard" and com[2] == "easy":
        print(f'''---------
| {main_list[0]} {main_list[1]} {main_list[2]} |
| {main_list[3]} {main_list[4]} {main_list[5]} |
| {main_list[6]} {main_list[7]} {main_list[8]} |
---------''')
        ans = com_vs_com(level = 7)
        if ans == True:
            k = 1
    


    


        

       

        
