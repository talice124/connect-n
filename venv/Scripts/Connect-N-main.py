import numpy as np
MOVE1 = 1
MOVE2 = 2
BOARD_HEIGHT = 8
BOARD_LENGTH = 11
MINIMUM_WINNING_SEQUENCE = 4
MAXIMUM_WINNING_SEQUENCE = 8
EMPTY_STRING = ""
COLUMN_FULL = "column_is_full"
BOARD_FULL  = "Board_is_full"
WHAT_FIRST_PLAYER_NAME = "What is the first player's name?"
WHAT_SECOND_PLAYER_NAME = "What is the second player's name?"
WHAT_SIZE_WINNING_SEQUENCE = "What is the size of the winning sequense? (4-8)"
PLEASE_INSERT_NUMBER_4_TO_8 = "Please insert a number between 4 and 8"
THIS_NOT_NUMBER_4_TO_8 = "This is not a number. Please insert a number between 4 and 8"
WHICH_COLUMN_NEXT_MOVE = "Which column do you choose to make your next move? (1-11)"
CANT_PUT_DISC_COLUMN_FULL = "Can't put a disc there, column is full."
PLEASE_INSERT_COLUMN_1_TO_11 = "Please insert a column number between 1 to 11"
BOARD_FULL_GAME_OVER = "Board is full. Game over"
THIS_NOT_NUMBER_1_TO_11 = "This is not a number. Please insert a column number between 1 to 11"
WON = "Won!"
GAME_OVER = "Game Over"

class Player:
    def __init__(self, name, move):
        self.name = name
        self.move = move


class Game:
    def __init__(self, string_size, name1, name2):
        self.player1 = Player(name1,MOVE1)
        self.player2 = Player(name2,MOVE2)
        self.N = int(string_size)
        # initialize board as a 11*8 array with 0 in it for empty spots
        self.board = []
        for i in range(BOARD_HEIGHT):
            current_column_list = []
            for j in range(BOARD_LENGTH):
                current_column_list.append(0)
            self.board.append(current_column_list)

    def did_move_win(self,player):
    # check for sequence in the rows
        for i in range(BOARD_HEIGHT):
            how_many_in_a_row = 0
            for j in range(BOARD_LENGTH):
                if (self.board[i][j] == player.move):
                    how_many_in_a_row += 1
                    if (how_many_in_a_row == self.N):
                        return True
                else:
                    how_many_in_a_row = 0

     # now check if there's a sequence in the columns
    # This code is very similar to the code chunk of the rows but not the same
    # It can't be put into a single function
    # This one starts with for j in range and the other one starts with for i in range
        for j in range(BOARD_LENGTH):
            how_many_in_a_row = 0
            for i in range(BOARD_HEIGHT):
                if (self.board[i][j] == player.move):
                    how_many_in_a_row += 1
                    if (how_many_in_a_row == self.N):
                        return True
                else:
                    how_many_in_a_row = 0

    # now check for a sequence in the diagonals
    # first make a list of diagonals
        diagonals = []
        for i in range((-1*BOARD_LENGTH+1),BOARD_LENGTH):
            diag = np.diagonal(self.board,i)
            diag2 = np.fliplr(self.board).diagonal(i)
            if (diag.size != 0):
                diagonals.append(diag)
            if (diag2.size != 0):
                diagonals.append(diag2)

        # now go over diagonals and check if any of them is a win
        for sequence in diagonals:
            how_many_in_a_row = 0
            for i in range(BOARD_LENGTH):
                if (i < sequence.size):
                    if (sequence[i] == player.move):
                        how_many_in_a_row += 1
                        if (how_many_in_a_row == self.N):
                            return True
                else:
                    how_many_in_a_row = 0

        return False


    # kukuku change to work with range instead of with 7-j https://docs.python.org/3/library/functions.html#func-range
    def make_move(self,column_number,player):
        for j in range(8):
            if (self.board[7-j][column_number] == 0):
                self.board[7-j][column_number] = player.move
                return j

        answer = EMPTY_STRING
        if (self.board[0][column_number] != 0): # column full
            answer = COLUMN_FULL
        full_columns = 0
        for i in range(11):
            if (self.board[0][i] != 0): #column full
                full_columns += 1
        if (full_columns == 11): # board is full
            answer = BOARD_FULL
        return answer





class Display:
    def __init__(self):
        name1 = name2 = N = EMPTY_STRING
        while (name1 == EMPTY_STRING):
            name1 = self.Show_message_to_player_with_response(WHAT_FIRST_PLAYER_NAME)
        while (name2 == EMPTY_STRING):
            name2 = self.Show_message_to_player_with_response(WHAT_SECOND_PLAYER_NAME)
        while (N == EMPTY_STRING):
            N = self.Show_message_to_player_with_response(WHAT_SIZE_WINNING_SEQUENCE)
            try:
                # check input value
                int_val = int(N)
                if (type(int_val) != int):
                    print(PLEASE_INSERT_NUMBER_4_TO_8)
                    N = EMPTY_STRING
                    continue
                else:   # kukuku check if should change | to the word OR
                    if ((int_val > MAXIMUM_WINNING_SEQUENCE) or (int_val < MINIMUM_WINNING_SEQUENCE)):
                        print(PLEASE_INSERT_NUMBER_4_TO_8)
                        N = EMPTY_STRING
                        continue
            except ValueError:
                print(THIS_NOT_NUMBER_4_TO_8)
                N = EMPTY_STRING
        self.my_Game = Game(N,name1,name2)
        self.Print_board()

    def Print_board(self):
        for i in range(BOARD_HEIGHT):
            my_string = EMPTY_STRING
            for j in range(BOARD_LENGTH):
                if (self.my_Game.board[i][j] == 1):
                    to_board = "X"
                elif (self.my_Game.board[i][j] ==2):
                    to_board = "O"
                else:
                    to_board = "."
                my_string += "|"+to_board
                if (j == BOARD_LENGTH-1):
                    my_string += "|"
                    print(my_string)

    def Show_message_to_player_with_response(self, message):
        val = input(message)
        return val

    def Get_move_from_player(self,player):
        need_column = True
        while (need_column):
            val = input(WHICH_COLUMN_NEXT_MOVE)
            try:
            # check input value
                int_val = int(val)
                if ((int_val > BOARD_LENGTH) or (int_val <1)):
                    print(PLEASE_INSERT_COLUMN_1_TO_11)
                    continue
                info = self.my_Game.make_move(int_val-1, player)
                if (info == COLUMN_FULL):
                    print(CANT_PUT_DISC_COLUMN_FULL)
                else:
                    if (info == BOARD_FULL):
                        print(BOARD_FULL_GAME_OVER)
                        return info
                    else:
                        need_column = False
            except ValueError:
                print(THIS_NOT_NUMBER_1_TO_11)

        self.Print_board()



if __name__ == "__main__":
    my_display = Display()
    for i in range(44):
        my_display.Get_move_from_player(my_display.my_Game.player1)
        if (my_display.my_Game.did_move_win(my_display.my_Game.player1)):
            print(my_display.my_Game.player1.name, WON)
            break
        my_display.Get_move_from_player(my_display.my_Game.player2)
        if (my_display.my_Game.did_move_win(my_display.my_Game.player2)):
            print(my_display.my_Game.player2.name, WON)
            break

    print(GAME_OVER)




