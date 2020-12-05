class Player:
    def __init__(self, name):
        self.name = name

    def Make_move(self):
        pass


class Game:
    def __init__(self, string_size, name1, name2):
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.N = string_size
        # initialize board as a 11*8 array with 0 in it for empty spots
        self.board = []
        for i in range(8):
            current_column_list = []
            for j in range(11):
                current_column_list.append(0)
            self.board.append(current_column_list)

    def Did_move_win(self):
        pass

    def make_move(self,column_number,player):
        if (self.player1.name == player):
            player_move = 'X'
        else:
            if (self.player2.name == player):
                player_move = 'O'
            else:
                raise Exception("Impossible player's name")

        for j in range(8):
            if (self.board[7-j][column_number] == 0):
                self.board[7-j][column_number] = player_move
                return j

        if (self.board[0][column_number] != 0): # column full
            return "column_is_full"






class Display:
    def __init__(self):
        name1 = self.Show_message_to_player_with_response("What is the first player's name?")
        name2 = self.Show_message_to_player_with_response("What is the second player's name?")
        N = self.Show_message_to_player_with_response("What is the size of the winning sequense? (4-8)")
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
        Val = input("Which column do you choose to make your next move?")
        self.my_Game.make_move(int(Val), player)
        self.Print_board()



if __name__ == "__main__":
    my_display = Display()
    my_display.Get_move_from_player(my_display.my_Game.player1.name)



