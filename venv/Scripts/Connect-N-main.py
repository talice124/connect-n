import numpy as np

class Player:
    def __init__(self, name, move):
        self.name = name
        self.move = move

    def Make_move(self):
        pass


class Game:
    def __init__(self, string_size, name1, name2):
        self.player1 = Player(name1,'1')
        self.player2 = Player(name2,'2')
        self.N = int(string_size)
        # initialize board as a 11*8 array with 0 in it for empty spots
        self.board = []
        for i in range(8):
            current_column_list = []
            for j in range(11):
                current_column_list.append(0)
            self.board.append(current_column_list)

    def Did_move_win(self,player):
    # check for sequence in the rows
        for i in range(8):
            how_many_in_a_row = 0
            for j in range(11):
                if (self.board[i][j] == player.move):
                    how_many_in_a_row += 1
                    if (how_many_in_a_row == self.N):
                        return True
                else:
                    how_many_in_a_row = 0

     # now check if there's a sequence in the columns
        for j in range(11):
            how_many_in_a_row = 0
            for i in range(8):
                if (self.board[i][j] == player.move):
                    how_many_in_a_row += 1
                    if (how_many_in_a_row == self.N):
                        return True
                else:
                    how_many_in_a_row = 0

    # now check for a sequence in the diagonals
    # first make a list of diagonals
        a = []
        for i in range(-10,11):
            diag = np.diagonal(self.board,i)
            diag2 = np.fliplr(self.board).diagonal(i)
            if (diag.size != 0):
                a.append(diag)
            if (diag2.size != 0):
                a.append(diag2)

        # now go over diagonals and check if any of them is a win
        for s in a:
            how_many_in_a_row = 0
            for i in range(11):
                if (i < s.size):
                    if (s[i] == player.move):
                        how_many_in_a_row += 1
                        if (how_many_in_a_row == self.N):
                            return True
                else:
                    how_many_in_a_row = 0

        return False


    def make_move(self,column_number,player):
        for j in range(8):
            if (self.board[7-j][column_number] == 0):
                self.board[7-j][column_number] = player.move
                return j

        answer = ""
        if (self.board[0][column_number] != 0): # column full
            answer = "column_is_full"
        full_columns = 0
        for i in range(11):
            if (self.board[0][i] != 0): #column full
                full_columns += 1
        if (full_columns == 11): # board is full
            answer = "Board_is_full"
        return answer





class Display:
    def __init__(self):
        name1 = name2 = N = ""
        while (name1 == ""):
            name1 = self.Show_message_to_player_with_response("What is the first player's name?")
        while (name2 == ""):
            name2 = self.Show_message_to_player_with_response("What is the second player's name?")
        while (N == ""):
            N = self.Show_message_to_player_with_response("What is the size of the winning sequense? (4-8)")
            try:
                # check input value
                int_val = int(N)
                if (type(int_val) != int):
                    print("Please insert a number between 4 and 8")
                    N = ""
                    continue
                else:
                    if ((int_val > 8) | (int_val < 4)):
                        print("Please insert a number between 4 and 8")
                        N = ""
                        continue
            except ValueError:
                print("This is not a number. Please insert a number between 4 and 8")
                N = ""
        self.my_Game = Game(N,name1,name2)
        self.Print_board()

    def Print_board(self):
        for i in range(8):
            my_string = ""
            for j in range(11):
                my_string += "|"+str(self.my_Game.board[i][j])
                if (j == 10):
                    my_string += "|"
                    print(my_string)

    def Show_message_to_player_with_response(self, message):
        Val = input(message)
        return Val

    def Get_move_from_player(self,player):
        need_column = True
        while (need_column):
            Val = input("Which column do you choose to make your next move? (1-11)")
            try:
            # check input value
                int_val = int(Val)
                if (type(int_val) != int):
                    print("Please insert a column number between 1 to 11")
                    continue
                else:
                    if ((int_val > 11) | (int_val <1)):
                        print("Please insert a column number between 1 to 11")
                        continue
                info = self.my_Game.make_move(int_val-1, player)
                if (info == "column_is_full"):
                    print("Can't put a disc there, column is full.")
                else:
                    if (info == "Board_is_full"):
                        print("Board is full. Game over")
                        return info
                    else:
                        need_column = False
            except ValueError:
                print("This is not a number. Please insert a column number between 1 to 11")

        self.Print_board()



if __name__ == "__main__":
    my_display = Display()
    for i in range(45):
        my_display.Get_move_from_player(my_display.my_Game.player1)
        my_display.Get_move_from_player(my_display.my_Game.player2)

    print(my_display.my_Game.Did_move_win(my_display.my_Game.player1))




