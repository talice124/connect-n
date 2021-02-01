from Connect_N_main import display

if __name__ == "__main__":
    my_display = display()
    for i in range(44):
        my_display.get_move_from_player(my_display.my_game.player1)
        if (my_display.my_game.did_move_win(my_display.my_game.player1)):
            break
        my_display.get_move_from_player(my_display.my_game.player2)
        if (my_display.my_game.did_move_win(my_display.my_game.player2)):
            break
