import pytest
from turtle import Turtle
from objects import Lines

@pytest.fixture
def lines():
    return Lines()

def test_draw_horizontal_line(mocker, lines):
    mock_goto = mocker.patch.object(Turtle, 'goto')
    mock_pendown = mocker.patch.object(Turtle, 'pendown')
    mock_setheading = mocker.patch.object(Turtle, 'setheading')
    mock_pensize = mocker.patch.object(Turtle, 'pensize')
    mock_forward = mocker.patch.object(Turtle, 'forward')
    mock_penup = mocker.patch.object(Turtle, 'penup')

    x, y, length = 0, 0, 100
    lines.draw_horizontal_line(x, y, length)

    mock_goto.assert_called_once_with(x, y)
    mock_pendown.assert_called_once()
    mock_setheading.assert_called_once_with(0)
    mock_pensize.assert_called_once_with(7)
    mock_forward.assert_called_once_with(length)
    mock_penup.assert_called()

def test_draw_vertical_line(mocker, lines):
    mock_goto = mocker.patch.object(Turtle, 'goto')
    mock_pendown = mocker.patch.object(Turtle, 'pendown')
    mock_setheading = mocker.patch.object(Turtle, 'setheading')
    mock_pensize = mocker.patch.object(Turtle, 'pensize')
    mock_forward = mocker.patch.object(Turtle, 'forward')
    mock_penup = mocker.patch.object(Turtle, 'penup')

    x, y, length = 0, 0, 100
    lines.draw_vertical_line(x, y, length)

    mock_goto.assert_called_once_with(x, y)
    mock_pendown.assert_called_once()
    mock_setheading.assert_called_once_with(90)
    mock_pensize.assert_called_once_with(7)
    mock_forward.assert_called_once_with(length)
    mock_penup.assert_called()