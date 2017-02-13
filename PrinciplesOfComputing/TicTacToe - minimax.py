"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    score_max = -2
    score_min = 2
    pos_max = (-1,-1)
    pos_min = (-1,-1)
    
    if board.check_win() != None:
        return SCORES[board.check_win()], (-1, -1)
        
    for move in board.get_empty_squares():
        board_copy = board.clone()
        board_copy.move(move[0],move[1],player)				
        
        temp_score, _ = mm_move(board_copy, provided.switch_player(player))
        
        if player == provided.PLAYERX:
            if temp_score > score_max:
                pos_max = move
                score_max = temp_score
            
        if player == provided.PLAYERO:
            if temp_score < score_min:
                pos_min = move
                score_min = temp_score    
    
    if player == provided.PLAYERX:
        return score_max, pos_max	
    elif player == provided.PLAYERO:
        return score_min, pos_min
    else:
        return 0, (-1,-1)
        
        
    
    
def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(2, provided.PLAYERO, move_wrapper, 1, False)

# print mm_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERX, provided.PLAYERX, provided.EMPTY],[provided.PLAYERO, provided.PLAYERO, provided.PLAYERO]]), provided.PLAYERO)

