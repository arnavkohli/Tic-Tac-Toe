#Tic Tac Toe using Minimax Algorithm

class Game():
    
    def evaluate(self, board, p1, p2):
        for i in range(3):
            if (board[i][0] == board[i][1] == board[i][2] != '-'):
                return 10 if board[i][0] == p1 else -10
            if (board[0][i] == board[1][i] == board[2][i] != '-'):
                return 10 if board[0][i] == p1 else -10
        if (board[0][0] == board[1][1] == board[2][2] != '-') or (board[2][0] == board[1][1] == board[0][2] != '-'):
            return 10 if board[1][1] == p1 else -10
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    return -1
        return 0

    def minimax(self, board, player, depth, p1, p2):
        if self.evaluate(board, p1, p2) != -1:
            if self.evaluate(board, p1, p2) == 10:
                return self.evaluate(board, p1, p2) - depth
            elif self.evaluate(board, p1, p2) == -10:
                return self.evaluate(board, p1, p2) + depth
            else:
                return 0
        if player == 1:
            value = -1000
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '-':
                        board[row][col] = p1
                        value = max(value , self.minimax(board, 2, depth + 1, p1, p2))
                        board[row][col] = '-'
            return value
        else:
            value = 1000
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '-':
                        board[row][col] = p2
                        value = min(value , self.minimax(board, 1, depth + 1, p1, p2))
                        board[row][col] = '-'
            return value

    def best_move(self, board, player, depth, p1, p2):
        move = [-1,-1]
        if player == 1:
            value = -1000
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '-':
                        board[row][col] = p1
                        if value < self.minimax(board, 2, depth + 1, p1, p2):
                            value = self.minimax(board, 2, depth + 1, p1, p2)
                            move = [row, col]
                        board[row][col] = '-'
            return move
        else:
            value = 1000
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '-':
                        board[row][col] = p2
                        if value > self.minimax(board, 1, depth + 1, p1, p2):
                            value = self.minimax(board, 1, depth + 1, p1, p2)
                            move = [row, col]
                        board[row][col] = '-'
            return move


    def print_board(self, board):
        for row in board:
            print (" ".join(row))
        print ('')

    def input_move(self):
        while True:
            pos = input()
            try:
                pos = int(pos)
            except:
                print ("Invalid choice, try again\n")
                continue
            if pos not in [i for i in range(1,10)]:
                print ("Invalid move, try again\n")
                continue
            if pos in range(1,4):
                play = [0, pos - 1]
            elif pos in range(4, 7):
                play = [1, pos - 4]
            elif pos in range(7,10):
                play = [2, pos - 7]
            return play

    def print_result(self, board, player, p1, p2):
        if player == 1:
            if self.evaluate(board, p1, p2) == 10:
                print("YOU WIN\n")
            elif self.evaluate(board, p1, p2) == -10:
                print("YOU LOSE\n")
            else:
                print("IT'S A TIE\n")
        else:
            if self.evaluate(board, p1, p2) == 10:
                print("YOU LOSE\n")
            elif self.evaluate(board, p1, p2) == -10:
                print("YOU WIN\n")
            else:
                print("IT'S A TIE\n")

    def play(self):
        loop = True
        while True:
            p1, p2 = '-', '-'
            current_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
            current_depth = 0
            while True:
                which_player = input("Do you want to be player 1 or player 2?\n")
                try:
                    which_player = int(which_player)
                except:
                    print("Invalid choice, try again\n")
                    continue
                if which_player not in [1, 2]:
                    print("Invalid choice, try again\n")
                    continue
                break
            while True:
                which_shape = input("Which shape do you want? X or O?\n").lower()
                if which_shape not in ['x','o']:
                    print("Invalid choice, try again\n")
                    continue
                break
            
            p1 = 'x' if which_shape == 'x' and which_player == 1 else 'o'
            p2 = 'x' if p1 == 'o' else 'o'
            
            print ("This is how the board looks like. You'll have to enter the position you want to place your shape in\n")
            for i in [1, 4, 7]:
                print("%s %s %s" % (i, i + 1, i + 2))
            print ("")
            while True:
                if which_player == 1:
                    while True:
                        print("IT'S YOUR MOVE")
                        play = self.input_move()
                        if current_board[play[0]][play[1]] != '-':
                            print("Position is occupied, try again\n")
                            continue
                        current_board[play[0]][play[1]] = p1
                        current_depth += 1
                        self.print_board(current_board)
                        break
                    if self.evaluate(current_board, p1, p2) != -1:
                        self.print_result(current_board, 1, p1, p2)
                        break
                    move = self.best_move(current_board, 2, current_depth, p1 , p2)
                    current_board[move[0]][move[1]] = p2
                    current_depth += 1
                    self.print_board(current_board)
                    if self.evaluate(current_board, p1, p2) != -1:
                        self.print_result(current_board, 1, p1, p2)
                        break

                else:
                    if loop:
                        print ("HOLD UP, IM THINKING!\n")
                    move = self.best_move(current_board, 1, current_depth, p1, p2)
                    current_board[move[0]][move[1]] = p1
                    current_depth += 1
                    self.print_board(current_board)
                    if self.evaluate(current_board, p1, p2) != -1:
                        self.print_result(current_board, 2, p1, p2)
                        break
                    while True:
                        print ("IT'S YOUR MOVE")
                        play = self.input_move()
                        if current_board[play[0]][play[1]] != '-':
                            print("Position is occupied, try again\n")
                            continue
                        current_board[play[0]][play[1]] = p2
                        current_depth += 1
                        self.print_board(current_board)
                        break
                    if self.evaluate(current_board, p1, p2) != -1:
                        self.print_result(current_board, 2, p1, p2)
                        break
                    loop = False
            while True:
                play_again = input("Play again? y/n\n").lower()
                if play_again == 'y':
                    break
                elif play_again == 'n':
                    print("Laters!")
                    exit()
                else:
                    print("Invalid response, try again\n")
                    continue
game = Game()
game.play()









