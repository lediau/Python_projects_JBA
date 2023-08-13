game = "         "
end_game = False


def empty_cells():
    if game.count(' ') > 0:
        return True
    return False


def three_in_a_row(token):
    win = token * 3
    # horizontal trio
    if (game.startswith(win) or
          game.endswith(win) or
            game[3:6] == win):
        return True

    # vertical trio
    elif (game[::3] == win or
          game[1::3] == win or
          game[2::3] == win):
        return True

    # diagonal trio
    elif (game[::4] == win or
          game[2:8:2] == win):
        return True

    return False


def playground():
    horizontal_lne = "---------"
    ind = 0
    line_1 = ['|']
    line_2 = ['|']
    line_3 = ['|']
    lines = [line_1, line_2, line_3]

    print(horizontal_lne)

    for i in range(0, 3):
        for j in range(1, 5):
            if j == 4:
                lines[i].append("|")  # right border
            else:
                lines[i].append(game[ind])
                ind += 1
        print(" ".join(lines[i]))

    print(horizontal_lne)


def perform_move(token):
    global game
    while True:
        try:
            move = input().split()
            move = [int(n) for n in move]
            index = 3 * (move[0] - 1) + (move[1] - 1)  # converting input to actual position
            if move[0] not in [1, 2, 3] or move[1] not in [1, 2, 3]:
                print("Coordinates should be from 1 to 3!")
            elif game[index] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                game = game[: index] + token + game[index + 1:]  # update the gameplay
                playground()
                break
        except Exception:
            print("You should enter numbers!")


def game_analysis():
    global end_game
    if abs(game.count('X') - game.count('O')) > 1 \
            or (three_in_a_row('X') and three_in_a_row('O')):
        print("Impossible")
        end_game = True
    elif three_in_a_row('X'):
        print("X wins")
        end_game = True
    elif three_in_a_row('O'):
        print("O wins")
        end_game = True
    else:
        if empty_cells():
            pass
        else:
            print("Draw")
            end_game = True


# MAIN PROGRAM
# print an empty grid
playground()

# playing the game round by round
turn = 0
tokens = ['X', 'O']
while not end_game:
    perform_move(tokens[turn % 2])
    turn += 1
    game_analysis()
