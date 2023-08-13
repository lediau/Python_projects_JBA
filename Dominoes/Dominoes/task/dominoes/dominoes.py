class Dominoes:
    dominoes = []
    snake = []

    def __init__(self):
        self.status = None
        self.player = None
        self.computer = None
        self.stock = None

    def domino_set(self):
        for x in range(0, 7):
            for y in range(0, 7):
                if x == y:
                    self.dominoes.append([x, y])
                if x > y:
                    self.dominoes.append([x, y])
        return self.dominoes

    def pieces(self):
        import random

        random.shuffle(self.domino_set())
        self.player = self.domino_set()[:7]
        self.computer = self.domino_set()[21:28]
        self.stock = self.domino_set()[7:21]

    def first_move(self):

        if max(self.player) > max(self.computer):
            self.snake.append(max(self.player))
            self.player.remove(max(self.player))
            self.status = "computer"
        else:
            self.snake.append(max(self.computer))
            self.computer.remove(max(self.computer))
            self.status = "player"

    def player_turn(self):
        print("Status: It's your turn to make a move. Enter your command.")
        while True:
            player_move = input()
            if not player_move.lstrip("-").isdigit():
                print("Invalid input. Please try again.")
            else:
                absolute_value = int(player_move[-1])
                player_move = int(player_move)
                if player_move > len(self.player):
                    print("Invalid input. Please try again.")
                else:
                    if player_move == 0:
                        self.player.append(self.stock[0])
                        self.stock.remove(self.stock[0])
                        break
                    elif player_move > 0:
                        self.snake.append(self.player[player_move - 1])
                        self.player.remove(self.player[player_move - 1])
                        break
                    elif player_move < 0:
                        self.snake.insert(0, self.player[absolute_value - 1])
                        self.player.remove(self.player[absolute_value - 1])
                        break
        self.status = "computer"

    def computer_turn(self):
        import random
        while True:
            computer_move = input("Status: Computer is about to make a move. Press Enter to continue...")
            if computer_move == "":
                computer_random = random.randint(0, len(self.computer) - 1)
                self.snake.append(self.computer[computer_random - 1])
                self.computer.remove(self.computer[computer_random - 1])
                break
            else:
                print("Invalid input. Please try again.")
            self.status = "player"

    def display(self):
        print("=" * 70)
        print(f"Stock size: {len(self.stock)}")
        print(f"Computer pieces: {len(self.computer)}\n")
        if len(self.snake) > 6:
            print(f"{self.snake[0]} {self.snake[1]} {self.snake[2]}...{self.snake[-3]} {self.snake[-2]} {self.snake[-1]}")
        else:
            print(f"{''.join(map(str, self.snake))}\n")
        print("Your pieces:")
        for n, piece in enumerate(self.player):
            print(f"{n + 1}: {piece}")
        print()

    def gameplay(self):
        if self.status == "player":
            return self.player_turn()
        elif self.status == "computer":
            return self.computer_turn()

    def draw_state(self):
        value_list = [x for xy in self.snake for x in xy]
        if value_list[0] == value_list[-1]:
            value = value_list.count(value_list[0])
            if value >= 8:
                return "Status: The game is over. It's a draw!"

    def game_state(self):
        if (len(self.player) == 0) and (len(self.computer) != 0):
            return "Status: The game is over. You won!"
        elif (len(self.computer) == 0) and (len(self.player) != 0):
            return "Status: The game is over. The computer won!"
        elif self.draw_state():
            print(self.draw_state())

    def play(self):
        self.pieces()
        self.first_move()
        self.display()
        while True:
            self.gameplay()
            if self.game_state():
                print(self.game_state())
                break
            self.display()


dominoes = Dominoes()
dominoes.play()
