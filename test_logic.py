import pytest
from logic import change_player, check_win, get_board_position, on_click

# FILEPATH: /home/laughinglambdas/Python/Projekty/TicTacToe-Python-Turtle/test_logic.py


def test_change_player():
    # Test when current_player is 'X'
    assert change_player(0, 0, 'X') == 'O'
    
    # Test when current_player is 'O'
    assert change_player(0, 0, 'O') == 'X'


def test_check_win():
    # Test when board has a winning combination for 'X'
    board = [['X', 'O', 'O'],
             ['X', 'X', 'O'],
             ['X', 'O', 'X']]
    assert check_win(board, 'X') == True
    
    # Test when board has a winning combination for 'O'
    board = [['O', 'X', 'O'],
             ['X', 'O', 'X'],
             ['O', 'X', 'O']]
    assert check_win(board, 'O') == True
    
    # Test when board does not have a winning combination
    board = [['X', 'O', 'O'],
             ['O', 'X', 'X'],
             ['X', 'O', 'O']]
    assert check_win(board, 'X') == False


def test_get_board_position():
    # Test when x and y are within the board range
    assert get_board_position(100, 200) == (0, 2)


def test_on_click():
    # Test when ongoing is False
    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]
    assert on_click(100, 200, board, 'X', False) == (board, 'O', False)
    
    # Test when ongoing is True and position is valid
    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]
    assert on_click(100, 200, board, 'X', True) == ([['', '', 'X'], ['', '', ''], ['', '', '']], 'O', True)
    