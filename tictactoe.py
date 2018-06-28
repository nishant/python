blank_board = " 1 | 2 | 3 \n---------\n 4 | 5 | 6 \n---------\n 7 | 8 | 9"
taken_pos = {'0'}
moves = [0,1,2,3,4,5,6,7,8,9]

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Board:
    def __init__(self):
        self.board = blank_board

    def print_board(self):
        print(self.board + '\n')

    def update_board(self, player, pos):
        new_board = self.board.replace(str(pos), player.symbol)
        self.board = new_board


def intro_prompt():
    print("\n\nTic-Tac-Toe Game!\n")
    p1_name = input("Player 1 - Enter Your Name: ")
    p1_symbol = input("Player 1 - Choose Symbol (X or O): " )

    while p1_symbol != "X" or p1_symbol != "O":
        if p1_symbol == "X" or p1_symbol == "O": 
            break
        p1_symbol = input("Invalid. Choose Symbol (X or O): " )
        
    p2_name = input("\nPlayer 2 - Enter Your Name: ")
    print('\n')
    
    if p1_symbol == "X": 
        p2_symbol = "O"
    else:
        p2_symbol = "X"
    
    return [p1_name, p1_symbol, p2_name, p2_symbol] 


def move_prompt(player):
    pos = input("{} - Enter a Position (1 - 9): ".format(player.name))
    
    while pos in taken_pos or not pos.isdigit() or len(pos) != 1:
        pos = input("Invalid. {} - Enter a Position (1 - 9): ".format(player.name))

    taken_pos.add(pos)
    moves[int(pos)] = player.symbol

    return pos


def in_a_row(pos1, pos2, pos3):
    if moves[pos1] == moves[pos2] == moves[pos3]:
        return moves[pos1]
    else:
        False


def check_winner(player):    
    if in_a_row(1,2,3) == player.symbol:
        return player
    elif in_a_row(4,5,6) == player.symbol:
        return player
    elif in_a_row(7,8,9) == player.symbol:
        return player
    elif in_a_row(1,4,7) == player.symbol:
        return player
    elif in_a_row(2,5,8) == player.symbol:
        return player
    elif in_a_row(3,6,9) == player.symbol:
        return player
    elif in_a_row(1,5,9) == player.symbol:
        return player
    elif in_a_row(3,5,7) == player.symbol:
        return player
    else:
        return False


def win_msg(player):
    print(player.name + " wins!\n")


def play_again():
    val = input("Do you want to play again? (Y or N): ")
   
    while val != 'Y' and val != 'N':
        val = input("Invalid. Do you want to play again? (Y or N): ")

    if val == 'Y':
        global taken_pos 
        taken_pos = {'0'}
        global moves 
        moves = [0,1,2,3,4,5,6,7,8,9]
        main() 
    else:
        exit()


def main():
    player_values = intro_prompt()

    player1 = Player(player_values[0], player_values[1])
    player2 = Player(player_values[2], player_values[3])

    board = Board()
    board.print_board()

    for _ in range(1,10):
        p1_pos = move_prompt(player1)
        print('\n')
        board.update_board(player1, p1_pos)
        board.print_board()

        win_check = check_winner(player1)
        if win_check != False:
            win_msg(win_check)
            play_again()

        p2_pos = move_prompt(player2)
        print('\n')
        board.update_board(player2, p2_pos)
        board.print_board()
        
        win_check = check_winner(player2)
        if win_check != False:
            win_msg(win_check)
            play_again()

    print("It's a Draw.")
    play_again()


if __name__ == "__main__":
    main()