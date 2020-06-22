"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #since X always starts then number of Xs will be either equal or greater to the number of Os
    #then if #Xs=#Os it is the turn of X, else if #Xs is greater than #Os then it is the turn of OSError
    nb_X=0
    nb_O=0
    i=0
    for i in range(3):
        for j in range(3):
            if board[i][j] ==X:
                nb_X+=1
            elif board[i][j]==O:
                nb_O+=1
    if nb_X==nb_O:
        return X
    elif nb_X>nb_O:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    S=[]
    for i in range(3):
        for j in range(3):
            if board [i][j]==EMPTY:
                S.append((i,j))
    return S
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i=action[0]
    j=action[1]
    if board[i][j] != EMPTY:
        raise NameError('Invalid action')
    board1=copy.deepcopy(board)
    board1[i][j]=player(board)
    return board1


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    if board[0][0]!=EMPTY and board[0][0]==board[0][1]==board[0][2]:
        return board[0][0]
    elif board[1][0]!=EMPTY and board[1][0]==board[1][1]==board[1][2]:
        return board[1][0]
    elif board[2][0]!=EMPTY and board[2][0]==board[2][1]==board[2][2]:
        return board[2][0]
    elif board[0][0]!=EMPTY and board[0][0]==board[1][0]==board[2][0]:
        return board[0][0]
    elif board[0][1]!=EMPTY and board[0][1]==board[1][1]==board[2][1]:
        return board[0][1]
    elif board[0][2]!=EMPTY and board[0][2]==board[1][2]==board[2][2]:
        return board[0][2]
    elif board[0][0]!=EMPTY and board[0][0]==board[1][1]==board[2][2]:
        return board[0][0]
    elif board[0][2]!=EMPTY and board[0][2]==board[1][1]==board[2][0]:
        return board[0][2]        
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None    
    if player(board)== X:
        return Max_Value(board)[1]
    if player(board)== O:
        return Min_Value(board)[1]
   
    




def Max_Value(board):
    if terminal(board):
        return [utility(board),None]
    v=[-100,None]
    for action in actions(board):
        y=Min_Value(result(board,action))
        if v[0]< y[0]:
            v=[y[0],action]
    return v    


def Min_Value(board):
    if terminal(board):
        return [utility(board),None]
    v=[100,None]
    for action in actions(board):
        y=Max_Value(result(board,action))
        if v[0] > y[0]:
            v=[y[0],action]
    return v      