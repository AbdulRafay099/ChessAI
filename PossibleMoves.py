import copy

def is_king_checked1(chessboard, king):
    all_enemy_moves = []
    under_check = False

    if king.name == "wK":

        all_enemy_moves = get_all_enemy_moves_ForCheck(chessboard, "white")
      
        for move in all_enemy_moves:
        
            if move[0] == king.alphaPosition and move[1] == king.numericPosition:
                under_check = True

    elif king.name == "bK":
        all_enemy_moves = get_all_enemy_moves_ForCheck(chessboard, "black")

        for move in all_enemy_moves:
            if move[0] == king.alphaPosition and move[1] == king.numericPosition:
                under_check = True

    return under_check

def get_all_enemy_moves_ForCheck(chess_board, side):
    total_moves = []
    
    if side == "white":
        for i in range(0, 8):
            for j in range(0, 8):                
                if chess_board[i][j].name == "bP":        
                    possible_moves = pawn_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name ==  "bR":
                    possible_moves = rook_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bN":
                    possible_moves = knight_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bB":
                    possible_moves = bishop_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bQ":
                    possible_moves = queen_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                    
    elif side == "black":
        for i in range(0, 8):
            for j in range(0, 8):                
                if chess_board[i][j].name == "wP":        
                    possible_moves = pawn_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name ==  "wR":
                    possible_moves = rook_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wN":
                    possible_moves = knight_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wB":
                    possible_moves = bishop_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wQ":
                    possible_moves = queen_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

    return total_moves


def get_all_enemy_moves(chess_board, side):
    total_moves = []
    
    if side == "white":
        for i in range(0, 8):
            for j in range(0, 8):                
                if chess_board[i][j].name == "bP":        
                    possible_moves = pawn_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name ==  "bR":
                    possible_moves = rook_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bN":
                    possible_moves = knight_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bB":
                    possible_moves = bishop_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bQ":
                    possible_moves = queen_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bK":
                    possible_moves = king_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves
                    
    elif side == "black":
        for i in range(0, 8):
            for j in range(0, 8):                
                if chess_board[i][j].name == "wP":        
                    possible_moves = pawn_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name ==  "wR":
                    possible_moves = rook_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wN":
                    possible_moves = knight_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wB":
                    possible_moves = bishop_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wQ":
                    possible_moves = queen_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wK":
                    possible_moves = king_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

    return total_moves       


def get_all_moves(chess_board, playerTurn, piece):
    
    total_moves = []

    if(playerTurn == "White"):
    
        for i in range(0, 8):
            for j in range(0, 8):

                if piece == "P":        
                    possible_moves = pawn_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif piece ==  "R":
                    possible_moves = rook_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif piece == "N":
                    possible_moves = knight_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif piece == "B":
                    possible_moves = bishop_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif piece == "Q":
                    possible_moves = queen_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif piece == "K":
                    possible_moves = king_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves
               
                
    if(playerTurn == "Black"):
    
        for i in range(0, 8):
            for j in range(0, 8):

                if piece == "P":        
                    possible_moves = pawn_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves


                elif piece == "R":
                    possible_moves = rook_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif piece == "N":
                    possible_moves = knight_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif piece == "B":
                    possible_moves = bishop_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif piece == "Q":
                    possible_moves = queen_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif piece == "K":
                    possible_moves = king_moves(chess_board, chess_board[i][j])
                    total_moves += possible_moves
                          
    return total_moves


def get_valid_moves(chess_board, piece):
           
    if piece.name == "wP":        
        possible_moves = pawn_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])

    elif piece.name ==  "wR":
        possible_moves = rook_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])

    elif piece.name == "wN":
        possible_moves = knight_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])

    elif piece.name == "wB":
        possible_moves = bishop_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])

    elif piece.name == "wQ":
        possible_moves = queen_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])

    elif piece.name == "wK":
        possible_moves = king_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])               

    if piece.name == "bP":        
        possible_moves = pawn_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])

    elif piece.name == "bR":
        possible_moves = rook_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])

    elif piece.name == "bN":
        possible_moves = knight_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])

    elif piece.name == "bB":
        possible_moves = bishop_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])

    elif piece.name == "bQ":
        possible_moves = queen_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])

    elif piece.name == "bK":
        possible_moves = king_moves(chess_board, chess_board[piece.alphaPosition][piece.numericPosition])

    return possible_moves


def check_at_position(chess_board, king, new_alpha_position, new_numeric_position):
    all_enemy_moves = []
    under_check = False

    if king.name == "wK":
        all_enemy_moves = get_all_enemy_moves(chess_board, "white")
        for move in all_enemy_moves:
            # print(move,end=", ")
            if move[0] == new_alpha_position and move[1] == king.numericPosition:
                under_check = True

    elif king.name == "bK":
        all_enemy_moves = get_all_enemy_moves(chess_board, "black")
        for move in all_enemy_moves:
            if move[0] == king.alphaPosition and move[1] == king.numericPosition:
                under_check = True

    return under_check


def king_moves(chess_board, king):
    possible_moves = []

    # alphaPosition   --- X-Axis
    # numericPosition --- Y-Axis

    # Move Left
    if king.alphaPosition > 0:
        if( chess_board[king.alphaPosition - 1][king.numericPosition].name == "--" or
            chess_board[king.alphaPosition - 1][king.numericPosition].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition - 1][king.numericPosition] = copy.deepcopy(new_chess_board[king.alphaPosition][king.numericPosition])
            
            new_chess_board[king.alphaPosition - 1][king.numericPosition].alphaPosition = king.alphaPosition - 1
            new_chess_board[king.alphaPosition - 1][king.numericPosition].numericPosition = king.numericPosition

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition - 1][king.numericPosition])
            
            if check == False:

                if(chess_board[king.alphaPosition-1][king.numericPosition].name[1] != "K"):
                    possible_moves.append((king.alphaPosition - 1, king.numericPosition))

    # Move Right
    if king.alphaPosition < 7:
        if( chess_board[king.alphaPosition + 1][king.numericPosition].name == "--" or
            chess_board[king.alphaPosition + 1][king.numericPosition].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition + 1][king.numericPosition] = copy.deepcopy(new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition + 1][king.numericPosition].alphaPosition = king.alphaPosition + 1
            new_chess_board[king.alphaPosition + 1][king.numericPosition].numericPosition = king.numericPosition

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition + 1][king.numericPosition])
            
            if check == False:

                if(chess_board[king.alphaPosition+1][king.numericPosition].name[1] != "K"):
                    possible_moves.append((king.alphaPosition + 1, king.numericPosition))

    # Move Up
    if king.numericPosition > 0:
        if( chess_board[king.alphaPosition][king.numericPosition - 1].name == "--" or
            chess_board[king.alphaPosition][king.numericPosition-1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition][king.numericPosition-1] = copy.deepcopy(new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition][king.numericPosition-1].alphaPosition = king.alphaPosition
            new_chess_board[king.alphaPosition][king.numericPosition-1].numericPosition = king.numericPosition-1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition][king.numericPosition-1])
            
            if check == False:

                if(chess_board[king.alphaPosition][king.numericPosition-1].name[1] != "K"):
                    possible_moves.append((king.alphaPosition, king.numericPosition - 1))

    # Move Down
    if king.numericPosition < 7:
        if( chess_board[king.alphaPosition][king.numericPosition + 1].name == "--" or
            chess_board[king.alphaPosition][king.numericPosition + 1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition][king.numericPosition+1] = copy.deepcopy(new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition][king.numericPosition+1].alphaPosition = king.alphaPosition
            new_chess_board[king.alphaPosition][king.numericPosition+1].numericPosition = king.numericPosition+1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition][king.numericPosition+1])
            
            if check == False:

                if(chess_board[king.alphaPosition][king.numericPosition+1].name[1] != "K"):
                    possible_moves.append((king.alphaPosition, king.numericPosition + 1))

    # Move Up_Right
    if king.alphaPosition > 0 and king.numericPosition < 7:
        if( chess_board[king.alphaPosition - 1][king.numericPosition + 1].name == "--" or
            chess_board[king.alphaPosition - 1][king.numericPosition+1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition - 1][king.numericPosition+1] = copy.deepcopy(new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition-1][king.numericPosition+1].alphaPosition = king.alphaPosition-1
            new_chess_board[king.alphaPosition-1][king.numericPosition+1].numericPosition = king.numericPosition+1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition - 1][king.numericPosition+1])
            
            if check == False:

                if(chess_board[king.alphaPosition-1][king.numericPosition+1].name[1] != "K"):
                    possible_moves.append((king.alphaPosition - 1, king.numericPosition + 1))

    # Move Up_Left
    if king.alphaPosition > 0 and king.numericPosition > 0:
        if( chess_board[king.alphaPosition - 1][king.numericPosition - 1].name == "--" or
            chess_board[king.alphaPosition - 1][king.numericPosition-1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition - 1][king.numericPosition-1] = copy.deepcopy(new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition-1][king.numericPosition-1].alphaPosition = king.alphaPosition-1
            new_chess_board[king.alphaPosition-1][king.numericPosition-1].numericPosition = king.numericPosition-1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition - 1][king.numericPosition-1])
            
            if check == False:

                if(chess_board[king.alphaPosition-1][king.numericPosition-1].name[1] != "K"):
                    possible_moves.append((king.alphaPosition - 1, king.numericPosition - 1))

    # Move Down_Right
    if king.alphaPosition < 7 and king.numericPosition < 7:
        if( chess_board[king.alphaPosition + 1][king.numericPosition + 1].name == "--" or
            chess_board[king.alphaPosition + 1][king.numericPosition+1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition + 1][king.numericPosition+1] = copy.deepcopy(new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition+1][king.numericPosition+1].alphaPosition = king.alphaPosition+1
            new_chess_board[king.alphaPosition+1][king.numericPosition+1].numericPosition = king.numericPosition+1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition + 1][king.numericPosition+1])
            
            if check == False:

                if(chess_board[king.alphaPosition+1][king.numericPosition+1].name[1] != "K"):
                    possible_moves.append((king.alphaPosition + 1, king.numericPosition + 1))

    # Move Down_Left
    if king.alphaPosition < 7 and king.numericPosition > 0:
        if( chess_board[king.alphaPosition + 1][king.numericPosition - 1].name == "--" or
            chess_board[king.alphaPosition + 1][king.numericPosition-1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition + 1][king.numericPosition-1] = copy.deepcopy(new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition+1][king.numericPosition-1].alphaPosition = king.alphaPosition+1
            new_chess_board[king.alphaPosition+1][king.numericPosition-1].numericPosition = king.numericPosition-1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition + 1][king.numericPosition-1])
            
            if check == False:
                if(chess_board[king.alphaPosition+1][king.numericPosition-1].name[1] != "K"):
                    possible_moves.append((king.alphaPosition + 1, king.numericPosition - 1))

    return possible_moves


def queen_moves(chess_board, queen):
    possible_moves = []

    # alphaPosition   --- X-Axis
    # numericPosition --- Y-Axis

    # Move Up
    for index in range(1, 8):
        if queen.alphaPosition - index >= 0:
            
            # If own piece in front of queen then break
            if(chess_board[queen.alphaPosition - index][queen.numericPosition].name[0] == queen.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[queen.alphaPosition - index][queen.numericPosition].name[0] != queen.name[0]
               and chess_board[queen.alphaPosition - index][queen.numericPosition].name != "--"):
                toContinue = False
        
        if queen.alphaPosition - index >= 0:

            if(chess_board[queen.alphaPosition-index][queen.numericPosition].name[1] != "K"):
                possible_moves.append((queen.alphaPosition - index, queen.numericPosition))
                if(toContinue == False):
                    break

    # Move Down
    for index in range(1, 8):
        if queen.alphaPosition + index < 8:
            
            # If own piece in front of queen then break
            if(chess_board[queen.alphaPosition + index][queen.numericPosition].name[0] == queen.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[queen.alphaPosition + index][queen.numericPosition].name[0] != queen.name[0]
               and chess_board[queen.alphaPosition + index][queen.numericPosition].name != "--"):
                toContinue = False
        
        if queen.alphaPosition + index < 8:

            if(chess_board[queen.alphaPosition+index][queen.numericPosition].name[1] != "K"):
                possible_moves.append((queen.alphaPosition + index, queen.numericPosition))
                if(toContinue == False):
                    break

    # Move Left
    for index in range(1, 8):
        if queen.numericPosition - index >= 0:
            
            # If own piece in front of queen then break
            if(chess_board[queen.alphaPosition][queen.numericPosition - index].name[0] == queen.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[queen.alphaPosition][queen.numericPosition - index].name[0] != queen.name[0]
               and chess_board[queen.alphaPosition][queen.numericPosition - index].name != "--"):
                toContinue = False
        
        if queen.numericPosition - index >= 0:

            if(chess_board[queen.alphaPosition][queen.numericPosition-index].name[1] != "K"):
                possible_moves.append((queen.alphaPosition, queen.numericPosition - index))
                if(toContinue == False):
                    break
    # Move Right
    for index in range(1, 8):
        if queen.numericPosition + index < 8:
            
            # If own piece in front of queen then break
            if(chess_board[queen.alphaPosition][queen.numericPosition + index].name[0] == queen.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[queen.alphaPosition][queen.numericPosition + index].name[0] != queen.name[0]
               and chess_board[queen.alphaPosition][queen.numericPosition + index].name != "--"):
                toContinue = False
        
        if queen.numericPosition + index < 8:

            if(chess_board[queen.alphaPosition][queen.numericPosition+index].name[1] != "K"):
                possible_moves.append((queen.alphaPosition, queen.numericPosition + index))
                if(toContinue == False):
                    break

    # Move Up_Right
    for index in range(1, 8):
        
        if queen.alphaPosition - index >= 0 and queen.numericPosition + index < 8:
            
            # If own piece in front of queen then break
            if(chess_board[queen.alphaPosition - index][queen.numericPosition + index].name[0] == queen.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[queen.alphaPosition - index][queen.numericPosition + index].name[0] != queen.name[0]
               and chess_board[queen.alphaPosition - index][queen.numericPosition + index].name != "--"):
                toContinue = False
        
        if queen.alphaPosition - index >= 0 and queen.numericPosition + index < 8:

            if(chess_board[queen.alphaPosition-index][queen.numericPosition+index].name[1] != "K"):
                possible_moves.append((queen.alphaPosition - index, queen.numericPosition + index))
                if(toContinue == False):
                    break

    # Move Up_Left
    for index in range(1, 8):
        if queen.alphaPosition - index >= 0 and queen.numericPosition - index >= 0:
            
            # If own piece in front of queen then break
            if(chess_board[queen.alphaPosition - index][queen.numericPosition - index].name[0] == queen.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[queen.alphaPosition - index][queen.numericPosition - index].name[0] != queen.name[0]
               and chess_board[queen.alphaPosition - index][queen.numericPosition - index].name != "--"):
                toContinue = False
        
        if queen.alphaPosition - index >= 0 and queen.numericPosition - index >= 0:

            if(chess_board[queen.alphaPosition-index][queen.numericPosition-index].name[1] != "K"):
                possible_moves.append((queen.alphaPosition - index, queen.numericPosition - index))
                if(toContinue == False):
                    break

    # Move Down_Right
    for index in range(1, 8):
        if queen.alphaPosition + index < 8 and queen.numericPosition + index < 8:
            
            # If own piece in front of queen then break
            if(chess_board[queen.alphaPosition + index][queen.numericPosition + index].name[0] == queen.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[queen.alphaPosition + index][queen.numericPosition + index].name[0] != queen.name[0]
               and chess_board[queen.alphaPosition + index][queen.numericPosition + index].name != "--"):
                toContinue = False
        
        if queen.alphaPosition + index < 8 and queen.numericPosition + index < 8:

            if(chess_board[queen.alphaPosition+index][queen.numericPosition+index].name[1] != "K"):
                possible_moves.append((queen.alphaPosition + index, queen.numericPosition + index))
                if(toContinue == False):
                    break

    # Move Down_Left
    for index in range(1, 8):
        if queen.alphaPosition + index < 8 and queen.numericPosition - index >= 0:
            
            # If own piece in front of queen then break
            if(chess_board[queen.alphaPosition + index][queen.numericPosition - index].name[0] == queen.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[queen.alphaPosition + index][queen.numericPosition - index].name[0] != queen.name[0]
               and chess_board[queen.alphaPosition + index][queen.numericPosition - index].name != "--"):
                toContinue = False
        
        if queen.alphaPosition + index < 8 and queen.numericPosition - index >= 0:

            if(chess_board[queen.alphaPosition+index][queen.numericPosition-index].name[1] != "K"):
                possible_moves.append((queen.alphaPosition + index, queen.numericPosition - index))
                if(toContinue == False):
                    break

    return possible_moves


def bishop_moves(chess_board, bishop):
    
    possible_moves = []
    
    # Move Up_Right
    for index in range(1, 8):
        
        if bishop.alphaPosition - index >= 0 and bishop.numericPosition + index < 8:
            
            # If own piece in front of queen then break
            if(chess_board[bishop.alphaPosition - index][bishop.numericPosition + index].name[0] == bishop.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[bishop.alphaPosition - index][bishop.numericPosition + index].name[0] != bishop.name[0]
               and chess_board[bishop.alphaPosition - index][bishop.numericPosition + index].name != "--"):
                toContinue = False
        
        if bishop.alphaPosition - index >= 0 and bishop.numericPosition + index < 8:

            if(chess_board[bishop.alphaPosition-index][bishop.numericPosition+index].name[1] != "K"):
                possible_moves.append((bishop.alphaPosition - index, bishop.numericPosition + index))
                if(toContinue == False):
                    break

    # Move Up_Left
    for index in range(1, 8):
        if bishop.alphaPosition - index >= 0 and bishop.numericPosition - index >= 0:
            
            # If own piece in front of queen then break
            if(chess_board[bishop.alphaPosition - index][bishop.numericPosition - index].name[0] == bishop.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[bishop.alphaPosition - index][bishop.numericPosition - index].name[0] != bishop.name[0]
               and chess_board[bishop.alphaPosition - index][bishop.numericPosition - index].name != "--"):
                toContinue = False
        
        if bishop.alphaPosition - index >= 0 and bishop.numericPosition - index >= 0:

            if(chess_board[bishop.alphaPosition-index][bishop.numericPosition-index].name[1] != "K"):
                possible_moves.append((bishop.alphaPosition - index, bishop.numericPosition - index))
                if(toContinue == False):
                    break

    # Move Down_Right
    for index in range(1, 8):
        if bishop.alphaPosition + index < 8 and bishop.numericPosition + index < 8:
            
            # If own piece in front of queen then break
            if(chess_board[bishop.alphaPosition + index][bishop.numericPosition + index].name[0] == bishop.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[bishop.alphaPosition + index][bishop.numericPosition + index].name[0] != bishop.name[0]
               and chess_board[bishop.alphaPosition + index][bishop.numericPosition + index].name != "--"):
                toContinue = False
        
        if bishop.alphaPosition + index < 8 and bishop.numericPosition + index < 8:

            if(chess_board[bishop.alphaPosition+index][bishop.numericPosition+index].name[1] != "K"):
                possible_moves.append((bishop.alphaPosition + index, bishop.numericPosition + index))
                if(toContinue == False):
                    break

    # Move Down_Left
    for index in range(1, 8):
        if bishop.alphaPosition + index < 8 and bishop.numericPosition - index >= 0:
            
            # If own piece in front of queen then break
            if(chess_board[bishop.alphaPosition + index][bishop.numericPosition - index].name[0] == bishop.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[bishop.alphaPosition + index][bishop.numericPosition - index].name[0] != bishop.name[0]
               and chess_board[bishop.alphaPosition + index][bishop.numericPosition - index].name != "--"):
                toContinue = False
        
        if bishop.alphaPosition + index < 8 and bishop.numericPosition - index >= 0:

            if(chess_board[bishop.alphaPosition-index][bishop.numericPosition-index].name[1] != "K"):
                possible_moves.append((bishop.alphaPosition + index, bishop.numericPosition - index))
                if(toContinue == False):
                    break

    return possible_moves


def rook_moves(chess_board, rook):
    
    possible_moves = []
    
    # Move Up
    for index in range(1, 8):
        if rook.alphaPosition - index >= 0:
            
            # If own piece in front of queen then break
            if(chess_board[rook.alphaPosition - index][rook.numericPosition].name[0] == rook.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[rook.alphaPosition - index][rook.numericPosition].name[0] != rook.name[0]
               and chess_board[rook.alphaPosition - index][rook.numericPosition].name != "--"):
                toContinue = False
        
        if rook.alphaPosition - index >= 0:

            if(chess_board[rook.alphaPosition - index][rook.numericPosition].name[1] != "K"):
                possible_moves.append((rook.alphaPosition - index, rook.numericPosition))
                if(toContinue == False):
                        break

    # Move Down
    for index in range(1, 8):
        if rook.alphaPosition + index < 8:
            
            # If own piece in front of queen then break
            if(chess_board[rook.alphaPosition + index][rook.numericPosition].name[0] == rook.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[rook.alphaPosition + index][rook.numericPosition].name[0] != rook.name[0]
               and chess_board[rook.alphaPosition + index][rook.numericPosition].name != "--"):
                toContinue = False
        
        if rook.alphaPosition + index < 8:

            if(chess_board[rook.alphaPosition + index][rook.numericPosition].name[1] != "K"):
                possible_moves.append((rook.alphaPosition + index, rook.numericPosition))
                if(toContinue == False):
                    break

    # Move Left
    for index in range(1, 8):
        if rook.numericPosition - index >= 0:
            
            # If own piece in front of queen then break
            if(chess_board[rook.alphaPosition][rook.numericPosition - index].name[0] == rook.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[rook.alphaPosition][rook.numericPosition - index].name[0] != rook.name[0]
               and chess_board[rook.alphaPosition][rook.numericPosition - index].name != "--"):
                toContinue = False
        
        if rook.numericPosition - index >= 0:

            if(chess_board[rook.alphaPosition][rook.numericPosition-index].name[1] != "K"):
                possible_moves.append((rook.alphaPosition, rook.numericPosition - index))
                if(toContinue == False):
                    break
    # Move Right
    for index in range(1, 8):
        if rook.numericPosition + index < 8:
            
            # If own piece in front of queen then break
            if(chess_board[rook.alphaPosition][rook.numericPosition + index].name[0] == rook.name[0]):
                break
                
            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if(chess_board[rook.alphaPosition][rook.numericPosition + index].name[0] != rook.name[0]
               and chess_board[rook.alphaPosition][rook.numericPosition + index].name != "--"):
                toContinue = False
        
        if rook.numericPosition + index < 8:

            if(chess_board[rook.alphaPosition][rook.numericPosition + index].name[1] != "K"):
                possible_moves.append((rook.alphaPosition, rook.numericPosition + index))
                if(toContinue == False):
                    break

    return possible_moves


def knight_moves(chess_board, knight):
    possible_moves = []

    # alphaPosition   --- X-Axis
    # numericPosition --- Y-Axis

    # Move Left Up
    if knight.alphaPosition > 1 and knight.numericPosition > 0:
        if( chess_board[knight.alphaPosition - 2][knight.numericPosition - 1].name == "--"
            or chess_board[knight.alphaPosition - 2][knight.numericPosition - 1].name[0] != knight.name[0]):
            
            if(chess_board[knight.alphaPosition - 2][knight.numericPosition-1].name[1] != "K"):
                possible_moves.append((knight.alphaPosition - 2, knight.numericPosition - 1))

    # Move Left Down
    if knight.alphaPosition > 1 and knight.numericPosition < 7:
        if( chess_board[knight.alphaPosition - 2][knight.numericPosition + 1].name == "--"
            or chess_board[knight.alphaPosition - 2][knight.numericPosition + 1].name[0] != knight.name[0]):
            
            if(chess_board[knight.alphaPosition - 2][knight.numericPosition+1].name[1] != "K"):
                possible_moves.append((knight.alphaPosition - 2, knight.numericPosition + 1))

    # Move Right Up
    if knight.alphaPosition < 6 and knight.numericPosition > 0:
        if( chess_board[knight.alphaPosition + 2][knight.numericPosition - 1].name == "--"
            or chess_board[knight.alphaPosition + 2][knight.numericPosition - 1].name[0] != knight.name[0]):
            
            if(chess_board[knight.alphaPosition + 2][knight.numericPosition-1].name[1] != "K"):
                possible_moves.append((knight.alphaPosition + 2, knight.numericPosition - 1))

    # Move Right Down
    if knight.alphaPosition < 6 and knight.numericPosition < 7:
        if( chess_board[knight.alphaPosition + 2][knight.numericPosition + 1].name == "--"
            or chess_board[knight.alphaPosition + 2][knight.numericPosition + 1].name[0] != knight.name[0]):
            
            if(chess_board[knight.alphaPosition + 2][knight.numericPosition+1].name[1] != "K"):
                possible_moves.append((knight.alphaPosition + 2, knight.numericPosition + 1))

    # Move Up Left
    if knight.numericPosition > 1 and knight.alphaPosition > 0:
        if( chess_board[knight.alphaPosition - 1][knight.numericPosition - 2].name == "--"
            or chess_board[knight.alphaPosition - 1][knight.numericPosition - 2].name[0] != knight.name[0]):

            if(chess_board[knight.alphaPosition - 2][knight.numericPosition-1].name[1] != "K"):
                possible_moves.append((knight.alphaPosition - 2, knight.numericPosition - 1))

    # Move Down Left
    if knight.numericPosition < 6 and knight.alphaPosition > 0:
        if( chess_board[knight.alphaPosition - 1][knight.numericPosition + 2].name == "--"
            or chess_board[knight.alphaPosition - 1][knight.numericPosition + 2].name[0] != knight.name[0]):
            
            if(chess_board[knight.alphaPosition - 1][knight.numericPosition+2].name[1] != "K"):
                possible_moves.append((knight.alphaPosition - 1, knight.numericPosition + 2))

    # Move Up Right
    if knight.numericPosition > 1 and knight.alphaPosition < 7:
        if( chess_board[knight.alphaPosition + 1][knight.numericPosition - 2].name == "--"
            or chess_board[knight.alphaPosition + 1][knight.numericPosition - 2].name[0] != knight.name[0]):
            
            if(chess_board[knight.alphaPosition +1][knight.numericPosition-2].name[1] != "K"):
                possible_moves.append((knight.alphaPosition + 1, knight.numericPosition - 2))

    # Move Down Right
    if knight.numericPosition < 6 and knight.alphaPosition < 7:
        if( chess_board[knight.alphaPosition + 1][knight.numericPosition + 2].name == "--"
            or chess_board[knight.alphaPosition + 1][knight.numericPosition + 2].name[0] != knight.name[0]):
            
            if(chess_board[knight.alphaPosition + 1][knight.numericPosition+2].name[1] != "K"):
                possible_moves.append((knight.alphaPosition + 1, knight.numericPosition + 2))

    return possible_moves


def pawn_moves(chess_board, pawn):
    possible_moves = []

    # Move Up White
    if pawn.name == "wP" and chess_board[pawn.alphaPosition - 1][pawn.numericPosition].name == "--":
        possible_moves.append((pawn.alphaPosition - 1, pawn.numericPosition))
        # checking if it is the first move of pawn
        if pawn.alphaPosition == 6:
            pawn.firstMove = False
            # moving pawn up
            if(chess_board[pawn.alphaPosition - 2][pawn.numericPosition].name == "--"):
                possible_moves.append((pawn.alphaPosition - 2, pawn.numericPosition))
            
    # Move Down Black
    elif pawn.name == "bP" and chess_board[pawn.alphaPosition + 1][pawn.numericPosition].name == "--":
        possible_moves.append((pawn.alphaPosition + 1, pawn.numericPosition))
        # checking if it is the first move of pawn
        if pawn.alphaPosition == 1:
            pawn.firstMove = False
            # moving pawn down
            if(chess_board[pawn.alphaPosition + 2][pawn.numericPosition].name == "--"):
                possible_moves.append((pawn.alphaPosition + 2, pawn.numericPosition))
      
    # Move Up-Left White
    if(pawn.alphaPosition - 1 >= 0 and pawn.numericPosition-1 >= 0):
        if( pawn.name == "wP" and chess_board[pawn.alphaPosition - 1][pawn.numericPosition-1].name[0] != pawn.name[0]
            and chess_board[pawn.alphaPosition - 1][pawn.numericPosition-1].name != "--"):
            
            if(chess_board[pawn.alphaPosition - 1][pawn.numericPosition-1].name[1] != "K"):
                possible_moves.append((pawn.alphaPosition - 1, pawn.numericPosition -1))
                # checking if it is the first move of pawn
                if pawn.alphaPosition == 6:
                    pawn.firstMove = False
            
    # Move Up-Right White
    if(pawn.alphaPosition - 1 >= 0 and pawn.numericPosition+1 <= 7):
        if( pawn.name == "wP" and chess_board[pawn.alphaPosition - 1][pawn.numericPosition+1].name[0] != pawn.name[0]
            and chess_board[pawn.alphaPosition - 1][pawn.numericPosition+1].name != "--"):
           
           if(chess_board[pawn.alphaPosition - 1][pawn.numericPosition+1].name[1] != "K"):
                possible_moves.append((pawn.alphaPosition - 1, pawn.numericPosition +1))
                # checking if it is the first move of pawn
                if pawn.alphaPosition == 6:
                    pawn.firstMove = False
            
    # Move Down-Left Black  
    if(pawn.alphaPosition + 1 <= 7 and pawn.numericPosition-1 >= 0):
        if( pawn.name == "bP" and chess_board[pawn.alphaPosition + 1][pawn.numericPosition - 1].name[0] != pawn.name[0]
            and chess_board[pawn.alphaPosition + 1][pawn.numericPosition-1].name != "--"):

           if(chess_board[pawn.alphaPosition + 1][pawn.numericPosition-1].name[1] != "K"):
                possible_moves.append((pawn.alphaPosition + 1, pawn.numericPosition -1))
                # checking if it is the first move of pawn
                if pawn.alphaPosition == 1:
                    pawn.firstMove = False
            
    # Move Down-Right Black     
    if(pawn.alphaPosition + 1 <= 7 and pawn.numericPosition+1 <= 7):
        if( pawn.name == "bP" and chess_board[pawn.alphaPosition + 1][pawn.numericPosition + 1].name[0] != pawn.name[0]
            and chess_board[pawn.alphaPosition + 1][pawn.numericPosition+1].name != "--"):
           

           if(chess_board[pawn.alphaPosition + 1][pawn.numericPosition+1].name[1] != "K"):
                possible_moves.append((pawn.alphaPosition + 1, pawn.numericPosition + 1))
                # checking if it is the first move of pawn
                if pawn.alphaPosition == 1:
                    pawn.firstMove = False

    return possible_moves







def king_moves1(chess_board, king):
    possible_moves = []

    # alphaPosition   --- X-Axis
    # numericPosition --- Y-Axis

    # Move Left
    if king.alphaPosition > 0:
        if (chess_board[king.alphaPosition - 1][king.numericPosition].name == "--" or
                chess_board[king.alphaPosition - 1][king.numericPosition].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition - 1][king.numericPosition] = copy.deepcopy(
                new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition - 1][king.numericPosition].alphaPosition = king.alphaPosition - 1
            new_chess_board[king.alphaPosition - 1][king.numericPosition].numericPosition = king.numericPosition

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition - 1][king.numericPosition])

            if check == False:
                possible_moves.append((king.alphaPosition - 1, king.numericPosition))

    # Move Right
    if king.alphaPosition < 7:
        if (chess_board[king.alphaPosition + 1][king.numericPosition].name == "--" or
                chess_board[king.alphaPosition + 1][king.numericPosition].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition + 1][king.numericPosition] = copy.deepcopy(
                new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition + 1][king.numericPosition].alphaPosition = king.alphaPosition + 1
            new_chess_board[king.alphaPosition + 1][king.numericPosition].numericPosition = king.numericPosition

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition + 1][king.numericPosition])

            if check == False:
                possible_moves.append((king.alphaPosition + 1, king.numericPosition))

    # Move Up
    if king.numericPosition > 0:
        if (chess_board[king.alphaPosition][king.numericPosition - 1].name == "--" or
                chess_board[king.alphaPosition][king.numericPosition - 1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition][king.numericPosition - 1] = copy.deepcopy(
                new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition][king.numericPosition - 1].alphaPosition = king.alphaPosition
            new_chess_board[king.alphaPosition][king.numericPosition - 1].numericPosition = king.numericPosition - 1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition][king.numericPosition - 1])

            if check == False:
                possible_moves.append((king.alphaPosition, king.numericPosition - 1))

    # Move Down
    if king.numericPosition < 7:
        if (chess_board[king.alphaPosition][king.numericPosition + 1].name == "--" or
                chess_board[king.alphaPosition][king.numericPosition + 1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition][king.numericPosition + 1] = copy.deepcopy(
                new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition][king.numericPosition + 1].alphaPosition = king.alphaPosition
            new_chess_board[king.alphaPosition][king.numericPosition + 1].numericPosition = king.numericPosition + 1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition][king.numericPosition + 1])

            if check == False:
                possible_moves.append((king.alphaPosition, king.numericPosition + 1))

    # Move Up_Right
    if king.alphaPosition > 0 and king.numericPosition < 7:
        if (chess_board[king.alphaPosition - 1][king.numericPosition + 1].name == "--" or
                chess_board[king.alphaPosition - 1][king.numericPosition + 1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition - 1][king.numericPosition + 1] = copy.deepcopy(
                new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition - 1][king.numericPosition + 1].alphaPosition = king.alphaPosition - 1
            new_chess_board[king.alphaPosition - 1][king.numericPosition + 1].numericPosition = king.numericPosition + 1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition - 1][king.numericPosition + 1])

            if check == False:

                possible_moves.append((king.alphaPosition - 1, king.numericPosition + 1))

    # Move Up_Left
    if king.alphaPosition > 0 and king.numericPosition > 0:
        if (chess_board[king.alphaPosition - 1][king.numericPosition - 1].name == "--" or
                chess_board[king.alphaPosition - 1][king.numericPosition - 1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition - 1][king.numericPosition - 1] = copy.deepcopy(
                new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition - 1][king.numericPosition - 1].alphaPosition = king.alphaPosition - 1
            new_chess_board[king.alphaPosition - 1][king.numericPosition - 1].numericPosition = king.numericPosition - 1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition - 1][king.numericPosition - 1])

            if check == False:

                possible_moves.append((king.alphaPosition - 1, king.numericPosition - 1))

    # Move Down_Right
    if king.alphaPosition < 7 and king.numericPosition < 7:
        if (chess_board[king.alphaPosition + 1][king.numericPosition + 1].name == "--" or
                chess_board[king.alphaPosition + 1][king.numericPosition + 1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition + 1][king.numericPosition + 1] = copy.deepcopy(
                new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition + 1][king.numericPosition + 1].alphaPosition = king.alphaPosition + 1
            new_chess_board[king.alphaPosition + 1][king.numericPosition + 1].numericPosition = king.numericPosition + 1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition + 1][king.numericPosition + 1])

            if check == False:
                possible_moves.append((king.alphaPosition + 1, king.numericPosition + 1))

    # Move Down_Left
    if king.alphaPosition < 7 and king.numericPosition > 0:
        if (chess_board[king.alphaPosition + 1][king.numericPosition - 1].name == "--" or
                chess_board[king.alphaPosition + 1][king.numericPosition - 1].name[0] != king.name[0]):

            new_chess_board = copy.deepcopy(chess_board)
            new_chess_board[king.alphaPosition + 1][king.numericPosition - 1] = copy.deepcopy(
                new_chess_board[king.alphaPosition][king.numericPosition])

            new_chess_board[king.alphaPosition + 1][king.numericPosition - 1].alphaPosition = king.alphaPosition + 1
            new_chess_board[king.alphaPosition + 1][king.numericPosition - 1].numericPosition = king.numericPosition - 1

            new_chess_board[king.alphaPosition][king.numericPosition].clear()
            check = is_king_checked1(new_chess_board, new_chess_board[king.alphaPosition + 1][king.numericPosition - 1])

            if check == False:
                possible_moves.append((king.alphaPosition + 1, king.numericPosition - 1))

    return possible_moves


def queen_moves1(chess_board, queen):
    possible_moves = []

    # alphaPosition   --- X-Axis
    # numericPosition --- Y-Axis

    # Move Up
    for index in range(1, 8):
        if queen.alphaPosition - index >= 0:

            # If own piece in front of queen then break
            if (chess_board[queen.alphaPosition - index][queen.numericPosition].name[0] == queen.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[queen.alphaPosition - index][queen.numericPosition].name[0] != queen.name[0]
                    and chess_board[queen.alphaPosition - index][queen.numericPosition].name != "--"):
                toContinue = False

        if queen.alphaPosition - index >= 0:

                possible_moves.append((queen.alphaPosition - index, queen.numericPosition))
                if (toContinue == False):
                    break

    # Move Down
    for index in range(1, 8):
        if queen.alphaPosition + index < 8:

            # If own piece in front of queen then break
            if (chess_board[queen.alphaPosition + index][queen.numericPosition].name[0] == queen.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[queen.alphaPosition + index][queen.numericPosition].name[0] != queen.name[0]
                    and chess_board[queen.alphaPosition + index][queen.numericPosition].name != "--"):
                toContinue = False

        if queen.alphaPosition + index < 8:

                possible_moves.append((queen.alphaPosition + index, queen.numericPosition))
                if (toContinue == False):
                    break

    # Move Left
    for index in range(1, 8):
        if queen.numericPosition - index >= 0:

            # If own piece in front of queen then break
            if (chess_board[queen.alphaPosition][queen.numericPosition - index].name[0] == queen.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[queen.alphaPosition][queen.numericPosition - index].name[0] != queen.name[0]
                    and chess_board[queen.alphaPosition][queen.numericPosition - index].name != "--"):
                toContinue = False

        if queen.numericPosition - index >= 0:

                possible_moves.append((queen.alphaPosition, queen.numericPosition - index))
                if (toContinue == False):
                    break
    # Move Right
    for index in range(1, 8):
        if queen.numericPosition + index < 8:

            # If own piece in front of queen then break
            if (chess_board[queen.alphaPosition][queen.numericPosition + index].name[0] == queen.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[queen.alphaPosition][queen.numericPosition + index].name[0] != queen.name[0]
                    and chess_board[queen.alphaPosition][queen.numericPosition + index].name != "--"):
                toContinue = False

        if queen.numericPosition + index < 8:

                possible_moves.append((queen.alphaPosition, queen.numericPosition + index))
                if (toContinue == False):
                    break

    # Move Up_Right
    for index in range(1, 8):

        if queen.alphaPosition - index >= 0 and queen.numericPosition + index < 8:

            # If own piece in front of queen then break
            if (chess_board[queen.alphaPosition - index][queen.numericPosition + index].name[0] == queen.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[queen.alphaPosition - index][queen.numericPosition + index].name[0] != queen.name[0]
                    and chess_board[queen.alphaPosition - index][queen.numericPosition + index].name != "--"):
                toContinue = False

        if queen.alphaPosition - index >= 0 and queen.numericPosition + index < 8:

                possible_moves.append((queen.alphaPosition - index, queen.numericPosition + index))
                if (toContinue == False):
                    break

    # Move Up_Left
    for index in range(1, 8):
        if queen.alphaPosition - index >= 0 and queen.numericPosition - index >= 0:

            # If own piece in front of queen then break
            if (chess_board[queen.alphaPosition - index][queen.numericPosition - index].name[0] == queen.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[queen.alphaPosition - index][queen.numericPosition - index].name[0] != queen.name[0]
                    and chess_board[queen.alphaPosition - index][queen.numericPosition - index].name != "--"):
                toContinue = False

        if queen.alphaPosition - index >= 0 and queen.numericPosition - index >= 0:

                possible_moves.append((queen.alphaPosition - index, queen.numericPosition - index))
                if (toContinue == False):
                    break

    # Move Down_Right
    for index in range(1, 8):
        if queen.alphaPosition + index < 8 and queen.numericPosition + index < 8:

            # If own piece in front of queen then break
            if (chess_board[queen.alphaPosition + index][queen.numericPosition + index].name[0] == queen.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[queen.alphaPosition + index][queen.numericPosition + index].name[0] != queen.name[0]
                    and chess_board[queen.alphaPosition + index][queen.numericPosition + index].name != "--"):
                toContinue = False

        if queen.alphaPosition + index < 8 and queen.numericPosition + index < 8:

                possible_moves.append((queen.alphaPosition + index, queen.numericPosition + index))
                if (toContinue == False):
                    break

    # Move Down_Left
    for index in range(1, 8):
        if queen.alphaPosition + index < 8 and queen.numericPosition - index >= 0:

            # If own piece in front of queen then break
            if (chess_board[queen.alphaPosition + index][queen.numericPosition - index].name[0] == queen.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[queen.alphaPosition + index][queen.numericPosition - index].name[0] != queen.name[0]
                    and chess_board[queen.alphaPosition + index][queen.numericPosition - index].name != "--"):
                toContinue = False

        if queen.alphaPosition + index < 8 and queen.numericPosition - index >= 0:

            if (chess_board[queen.alphaPosition + index][queen.numericPosition - index].name[1] != "K"):
                possible_moves.append((queen.alphaPosition + index, queen.numericPosition - index))
                if (toContinue == False):
                    break

    return possible_moves


def bishop_moves1(chess_board, bishop):
    possible_moves = []

    # Move Up_Right
    for index in range(1, 8):

        if bishop.alphaPosition - index >= 0 and bishop.numericPosition + index < 8:

            # If own piece in front of queen then break
            if (chess_board[bishop.alphaPosition - index][bishop.numericPosition + index].name[0] == bishop.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[bishop.alphaPosition - index][bishop.numericPosition + index].name[0] != bishop.name[0]
                    and chess_board[bishop.alphaPosition - index][bishop.numericPosition + index].name != "--"):
                toContinue = False

        if bishop.alphaPosition - index >= 0 and bishop.numericPosition + index < 8:

                possible_moves.append((bishop.alphaPosition - index, bishop.numericPosition + index))
                if (toContinue == False):
                    break

    # Move Up_Left
    for index in range(1, 8):
        if bishop.alphaPosition - index >= 0 and bishop.numericPosition - index >= 0:

            # If own piece in front of queen then break
            if (chess_board[bishop.alphaPosition - index][bishop.numericPosition - index].name[0] == bishop.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[bishop.alphaPosition - index][bishop.numericPosition - index].name[0] != bishop.name[0]
                    and chess_board[bishop.alphaPosition - index][bishop.numericPosition - index].name != "--"):
                toContinue = False

        if bishop.alphaPosition - index >= 0 and bishop.numericPosition - index >= 0:

                possible_moves.append((bishop.alphaPosition - index, bishop.numericPosition - index))
                if (toContinue == False):
                    break

    # Move Down_Right
    for index in range(1, 8):
        if bishop.alphaPosition + index < 8 and bishop.numericPosition + index < 8:

            # If own piece in front of queen then break
            if (chess_board[bishop.alphaPosition + index][bishop.numericPosition + index].name[0] == bishop.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[bishop.alphaPosition + index][bishop.numericPosition + index].name[0] != bishop.name[0]
                    and chess_board[bishop.alphaPosition + index][bishop.numericPosition + index].name != "--"):
                toContinue = False

        if bishop.alphaPosition + index < 8 and bishop.numericPosition + index < 8:

                possible_moves.append((bishop.alphaPosition + index, bishop.numericPosition + index))
                if (toContinue == False):
                    break

    # Move Down_Left
    for index in range(1, 8):
        if bishop.alphaPosition + index < 8 and bishop.numericPosition - index >= 0:

            # If own piece in front of queen then break
            if (chess_board[bishop.alphaPosition + index][bishop.numericPosition - index].name[0] == bishop.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[bishop.alphaPosition + index][bishop.numericPosition - index].name[0] != bishop.name[0]
                    and chess_board[bishop.alphaPosition + index][bishop.numericPosition - index].name != "--"):
                toContinue = False

        if bishop.alphaPosition + index < 8 and bishop.numericPosition - index >= 0:

                possible_moves.append((bishop.alphaPosition + index, bishop.numericPosition - index))
                if (toContinue == False):
                    break

    return possible_moves


def rook_moves1(chess_board, rook):
    possible_moves = []

    # Move Up
    for index in range(1, 8):
        if rook.alphaPosition - index >= 0:

            # If own piece in front of queen then break
            if (chess_board[rook.alphaPosition - index][rook.numericPosition].name[0] == rook.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[rook.alphaPosition - index][rook.numericPosition].name[0] != rook.name[0]
                    and chess_board[rook.alphaPosition - index][rook.numericPosition].name != "--"):
                toContinue = False

        if rook.alphaPosition - index >= 0:

                possible_moves.append((rook.alphaPosition - index, rook.numericPosition))
                if (toContinue == False):
                    break

    # Move Down
    for index in range(1, 8):
        if rook.alphaPosition + index < 8:

            # If own piece in front of queen then break
            if (chess_board[rook.alphaPosition + index][rook.numericPosition].name[0] == rook.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[rook.alphaPosition + index][rook.numericPosition].name[0] != rook.name[0]
                    and chess_board[rook.alphaPosition + index][rook.numericPosition].name != "--"):
                toContinue = False

        if rook.alphaPosition + index < 8:

                possible_moves.append((rook.alphaPosition + index, rook.numericPosition))
                if (toContinue == False):
                    break

    # Move Left
    for index in range(1, 8):
        if rook.numericPosition - index >= 0:

            # If own piece in front of queen then break
            if (chess_board[rook.alphaPosition][rook.numericPosition - index].name[0] == rook.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[rook.alphaPosition][rook.numericPosition - index].name[0] != rook.name[0]
                    and chess_board[rook.alphaPosition][rook.numericPosition - index].name != "--"):
                toContinue = False

        if rook.numericPosition - index >= 0:

                possible_moves.append((rook.alphaPosition, rook.numericPosition - index))
                if (toContinue == False):
                    break
    # Move Right
    for index in range(1, 8):
        if rook.numericPosition + index < 8:

            # If own piece in front of queen then break
            if (chess_board[rook.alphaPosition][rook.numericPosition + index].name[0] == rook.name[0]):
                break

            # If enemy piece in front of queen then its last possible move for queen
            toContinue = True
            if (chess_board[rook.alphaPosition][rook.numericPosition + index].name[0] != rook.name[0]
                    and chess_board[rook.alphaPosition][rook.numericPosition + index].name != "--"):
                toContinue = False

        if rook.numericPosition + index < 8:

                possible_moves.append((rook.alphaPosition, rook.numericPosition + index))
                if (toContinue == False):
                    break

    return possible_moves


def knight_moves1(chess_board, knight):
    possible_moves = []

    # alphaPosition   --- X-Axis
    # numericPosition --- Y-Axis

    # Move Left Up
    if knight.alphaPosition > 1 and knight.numericPosition > 0:
        if (chess_board[knight.alphaPosition - 2][knight.numericPosition - 1].name == "--"
                or chess_board[knight.alphaPosition - 2][knight.numericPosition - 1].name[0] != knight.name[0]):

                possible_moves.append((knight.alphaPosition - 2, knight.numericPosition - 1))

    # Move Left Down
    if knight.alphaPosition > 1 and knight.numericPosition < 7:
        if (chess_board[knight.alphaPosition - 2][knight.numericPosition + 1].name == "--"
                or chess_board[knight.alphaPosition - 2][knight.numericPosition + 1].name[0] != knight.name[0]):

                possible_moves.append((knight.alphaPosition - 2, knight.numericPosition + 1))

    # Move Right Up
    if knight.alphaPosition < 6 and knight.numericPosition > 0:
        if (chess_board[knight.alphaPosition + 2][knight.numericPosition - 1].name == "--"
                or chess_board[knight.alphaPosition + 2][knight.numericPosition - 1].name[0] != knight.name[0]):

                possible_moves.append((knight.alphaPosition + 2, knight.numericPosition - 1))

    # Move Right Down
    if knight.alphaPosition < 6 and knight.numericPosition < 7:
        if (chess_board[knight.alphaPosition + 2][knight.numericPosition + 1].name == "--"
                or chess_board[knight.alphaPosition + 2][knight.numericPosition + 1].name[0] != knight.name[0]):

                possible_moves.append((knight.alphaPosition + 2, knight.numericPosition + 1))

    # Move Up Left
    if knight.numericPosition > 1 and knight.alphaPosition > 0:
        if (chess_board[knight.alphaPosition - 1][knight.numericPosition - 2].name == "--"
                or chess_board[knight.alphaPosition - 1][knight.numericPosition - 2].name[0] != knight.name[0]):

                possible_moves.append((knight.alphaPosition - 2, knight.numericPosition - 1))

    # Move Down Left
    if knight.numericPosition < 6 and knight.alphaPosition > 0:
        if (chess_board[knight.alphaPosition - 1][knight.numericPosition + 2].name == "--"
                or chess_board[knight.alphaPosition - 1][knight.numericPosition + 2].name[0] != knight.name[0]):

                possible_moves.append((knight.alphaPosition - 1, knight.numericPosition + 2))

    # Move Up Right
    if knight.numericPosition > 1 and knight.alphaPosition < 7:
        if (chess_board[knight.alphaPosition + 1][knight.numericPosition - 2].name == "--"
                or chess_board[knight.alphaPosition + 1][knight.numericPosition - 2].name[0] != knight.name[0]):

                possible_moves.append((knight.alphaPosition + 1, knight.numericPosition - 2))

    # Move Down Right
    if knight.numericPosition < 6 and knight.alphaPosition < 7:
        if (chess_board[knight.alphaPosition + 1][knight.numericPosition + 2].name == "--"
                or chess_board[knight.alphaPosition + 1][knight.numericPosition + 2].name[0] != knight.name[0]):

                possible_moves.append((knight.alphaPosition + 1, knight.numericPosition + 2))

    return possible_moves


def pawn_moves1(chess_board, pawn):
    possible_moves = []

    # Move Up White
    if pawn.name == "wP" and chess_board[pawn.alphaPosition - 1][pawn.numericPosition].name == "--":
        possible_moves.append((pawn.alphaPosition - 1, pawn.numericPosition))
        # checking if it is the first move of pawn
        if pawn.alphaPosition == 6:
            pawn.firstMove = False
            # moving pawn up
            if (chess_board[pawn.alphaPosition - 2][pawn.numericPosition].name == "--"):
                possible_moves.append((pawn.alphaPosition - 2, pawn.numericPosition))

    # Move Down Black
    elif pawn.name == "bP" and chess_board[pawn.alphaPosition + 1][pawn.numericPosition].name == "--":
        possible_moves.append((pawn.alphaPosition + 1, pawn.numericPosition))
        # checking if it is the first move of pawn
        if pawn.alphaPosition == 1:
            pawn.firstMove = False
            # moving pawn down
            if (chess_board[pawn.alphaPosition + 2][pawn.numericPosition].name == "--"):
                possible_moves.append((pawn.alphaPosition + 2, pawn.numericPosition))

    # Move Up-Left White
    if (pawn.alphaPosition - 1 >= 0 and pawn.numericPosition - 1 >= 0):
        if (pawn.name == "wP" and chess_board[pawn.alphaPosition - 1][pawn.numericPosition - 1].name[0] != pawn.name[0]
                and chess_board[pawn.alphaPosition - 1][pawn.numericPosition - 1].name != "--"):

                possible_moves.append((pawn.alphaPosition - 1, pawn.numericPosition - 1))
                # checking if it is the first move of pawn
                if pawn.alphaPosition == 6:
                    pawn.firstMove = False

    # Move Up-Right White
    if (pawn.alphaPosition - 1 >= 0 and pawn.numericPosition + 1 <= 7):
        if (pawn.name == "wP" and chess_board[pawn.alphaPosition - 1][pawn.numericPosition + 1].name[0] != pawn.name[0]
                and chess_board[pawn.alphaPosition - 1][pawn.numericPosition + 1].name != "--"):


                possible_moves.append((pawn.alphaPosition - 1, pawn.numericPosition + 1))
                # checking if it is the first move of pawn
                if pawn.alphaPosition == 6:
                    pawn.firstMove = False

    # Move Down-Left Black
    if (pawn.alphaPosition + 1 <= 7 and pawn.numericPosition - 1 >= 0):
        if (pawn.name == "bP" and chess_board[pawn.alphaPosition + 1][pawn.numericPosition - 1].name[0] != pawn.name[0]
                and chess_board[pawn.alphaPosition + 1][pawn.numericPosition - 1].name != "--"):


                possible_moves.append((pawn.alphaPosition + 1, pawn.numericPosition - 1))
                # checking if it is the first move of pawn
                if pawn.alphaPosition == 1:
                    pawn.firstMove = False

    # Move Down-Right Black
    if (pawn.alphaPosition + 1 <= 7 and pawn.numericPosition + 1 <= 7):
        if (pawn.name == "bP" and chess_board[pawn.alphaPosition + 1][pawn.numericPosition + 1].name[0] != pawn.name[0]
                and chess_board[pawn.alphaPosition + 1][pawn.numericPosition + 1].name != "--"):


                possible_moves.append((pawn.alphaPosition + 1, pawn.numericPosition + 1))
                # checking if it is the first move of pawn
                if pawn.alphaPosition == 1:
                    pawn.firstMove = False

    return possible_moves


def get_all_check_moves(chess_board, side):
    total_moves = []

    if side == "white":
        for i in range(0, 8):
            for j in range(0, 8):
                if chess_board[i][j].name == "bP":
                    possible_moves = pawn_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bR":
                    possible_moves = rook_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bN":
                    possible_moves = knight_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bB":
                    possible_moves = bishop_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bQ":
                    possible_moves = queen_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "bK":
                    possible_moves = king_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

    elif side == "black":
        for i in range(0, 8):
            for j in range(0, 8):
                if chess_board[i][j].name == "wP":
                    possible_moves = pawn_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wR":
                    possible_moves = rook_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wN":
                    possible_moves = knight_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wB":
                    possible_moves = bishop_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wQ":
                    possible_moves = queen_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

                elif chess_board[i][j].name == "wK":
                    possible_moves = king_moves1(chess_board, chess_board[i][j])
                    total_moves += possible_moves

    return total_moves

    