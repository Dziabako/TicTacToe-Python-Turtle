from objects import Draw

drawer = Draw()

def change_player(x, y, current_player):

    # Determine the cell based on click position
    if -250 < x < -100:
        col = -175
    elif -100 < x < 100:
        col = 0
    elif 100 < x < 250:
        col = 175
    else:
        return

    if -250 < y < -100:
        row = -175
    elif -100 < y < 100:
        row = 0
    elif 100 < y < 250:
        row = 175
    else:
        return

    if current_player == "X":
        drawer.draw_x(col, row)
        current_player = "O"
    else:
        drawer.draw_o(col, row)
        current_player = "X"