import pytest
from unittest.mock import patch
from main import setup_game, screen, current_player, ongoing, text, draw_board, wrapper_on_click

@pytest.fixture
def setup(mocker):
    print("Running setup fixture")
    mocker.patch('main.text.clear_text', return_value=None)
    mocker.patch('main.text.display_player_turn', return_value=None)
    mocker.patch('main.draw_board', return_value=None)
    mocker.patch('main.screen.onscreenclick', return_value=None)
    
    setup_game()
    yield
    print("Finished setup fixture")


def test_setup_game_initializes_board(setup):
    from main import board, current_player, ongoing
    assert board == [['', '', ''], ['', '', ''], ['', '', '']]
    assert current_player == "X"
    assert ongoing == True


def test_setup_game_calls_clear_text(setup, mocker):
    mock_clear_text = mocker.patch('main.text.clear_text')
    setup_game()
    mock_clear_text.assert_called_once()


def test_setup_game_calls_display_player_turn(setup, mocker):
    mock_display_player_turn = mocker.patch('main.text.display_player_turn')
    setup_game()
    mock_display_player_turn.assert_called_once_with("X")


def test_setup_game_calls_draw_board(setup, mocker):
    mock_draw_board = mocker.patch('main.draw_board')
    setup_game()
    mock_draw_board.assert_called_once()


def test_setup_game_calls_onscreenclick(setup, mocker):
    mock_onscreenclick = mocker.patch('main.screen.onscreenclick')
    setup_game()
    mock_onscreenclick.assert_called_once_with(wrapper_on_click)


# Add additional tests for other functions and behaviors as needed
def test_click_outside_board_does_nothing(setup, mocker):
    mock_on_click = mocker.patch('main.on_click')
    wrapper_on_click(-300, 300)
    mock_on_click.assert_not_called()