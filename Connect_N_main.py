import numpy as np
import logging

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
PLAYER_WON_GAME_OVER = "%s Won! Game is over"
WON_GAME_OVER = "Won! Game is over"
FIRST_PLAYER_NAME = "First player's name is %s"
SECOND_PLAYER_NAME = "Second player's name is %s"
N_IS = 'N is %d'
PLAYER_TRIED_TO_PUT_DISC_AT_FULL_COLUMN = "%s tried to put a disc at column %d but the column is full"
PLAYER_PUT_DISC_ON_COLUMN = "%s put a disc on column %d"
LINE = "|"
DISK1 = "X"
DISK2 = "O"
DOT = "."

logging.basicConfig(filename='test.log', level=logging.DEBUG)

class player:
    def __init__(self, name, move):
        self.name = name
        self.move = move


class game:
    def __init__(self, string_size, name1, name2):
        self.player1 = player(name1,MOVE1)
        self.player2 = player(name2,MOVE2)
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
                        logging.info(PLAYER_WON_GAME_OVER, player.name)
                        print(player.name, WON_GAME_OVER)
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
                        logging.info(PLAYER_WON_GAME_OVER, player.name)
                        print(player.name, WON_GAME_OVER)
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
                            logging.info(PLAYER_WON_GAME_OVER,player.name)
                            print(player.name, WON_GAME_OVER)
                            return True
                else:
                    how_many_in_a_row = 0

        return False


    def make_move(self,column_number,player):
        for j in range(BOARD_HEIGHT):
            if (self.board[7-j][column_number] == 0):
                self.board[7-j][column_number] = player.move
                logging.info(PLAYER_PUT_DISC_ON_COLUMN,player.name,column_number+1)
                return j

        answer = EMPTY_STRING
        if (self.board[0][column_number] != 0): # column full
            answer = COLUMN_FULL
        full_columns = 0
        for i in range(BOARD_LENGTH):
            if (self.board[0][i] != 0): #column full
                full_columns += 1
        if (full_columns == BOARD_LENGTH): # board is full
            answer = BOARD_FULL
        return answer





class display:
    def __init__(self):
        name1 = name2 = N = EMPTY_STRING
        while (name1 == EMPTY_STRING):
            name1 = self.show_message_to_player_with_response(WHAT_FIRST_PLAYER_NAME)
        while (name2 == EMPTY_STRING):
            name2 = self.show_message_to_player_with_response(WHAT_SECOND_PLAYER_NAME)
        while (N == EMPTY_STRING):
            N = self.show_message_to_player_with_response(WHAT_SIZE_WINNING_SEQUENCE)
            try:
                # check input value
                int_val = int(N)
                if (type(int_val) != int):
                    print(PLEASE_INSERT_NUMBER_4_TO_8)
                    N = EMPTY_STRING
                    continue
                else:
                    if ((int_val > MAXIMUM_WINNING_SEQUENCE) or (int_val < MINIMUM_WINNING_SEQUENCE)):
                        print(PLEASE_INSERT_NUMBER_4_TO_8)
                        N = EMPTY_STRING
                        continue
            except ValueError:
                print(THIS_NOT_NUMBER_4_TO_8)
                N = EMPTY_STRING
        logging.info(FIRST_PLAYER_NAME,name1)
        logging.info(SECOND_PLAYER_NAME, name2)
        logging.info(N_IS, int_val)
        self.my_game = game(int_val,name1,name2)
        self.print_board()

    def print_board(self):
        my_string2 = LINE
        for j in range(BOARD_LENGTH):
            my_string2 += str(j+1) + LINE
        print(my_string2)
        for i in range(BOARD_HEIGHT):
            my_string = EMPTY_STRING
            for j in range(BOARD_LENGTH):
                if (self.my_game.board[i][j] == 1):
                    to_board = DISK1
                elif (self.my_game.board[i][j] ==2):
                    to_board = DISK2
                else:
                    to_board = DOT
                my_string += LINE + to_board
                if (j == BOARD_LENGTH-1):
                    my_string += LINE
                    print(my_string)
        print(my_string2)

    def show_message_to_player_with_response(self, message):
        val = input(message)
        return val

    def get_move_from_player(self,player):
        need_column = True
        while (need_column):
            val = input(WHICH_COLUMN_NEXT_MOVE)
            try:
            # check input value
                int_val = int(val)
                if ((int_val > BOARD_LENGTH) or (int_val <1)):
                    print(PLEASE_INSERT_COLUMN_1_TO_11)
                    continue
                info = self.my_game.make_move(int_val-1, player)
                if (info == COLUMN_FULL):
                    logging.info(PLAYER_TRIED_TO_PUT_DISC_AT_FULL_COLUMN,player.name,int_val-1)
                    print(CANT_PUT_DISC_COLUMN_FULL)
                else:
                    if (info == BOARD_FULL):
                        print(BOARD_FULL_GAME_OVER)
                        return info
                    else:
                        need_column = False
            except ValueError:
                print(THIS_NOT_NUMBER_1_TO_11)

        self.print_board()








