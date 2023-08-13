from random import choice
from string import ascii_lowercase

# universal variables
WORDS = ("python", "java", "swift", "javascript")
wins = 0
loses = 0


def one_round():
    global wins
    global loses
    attempts = 8                # available attempts for player
    correct = choice(WORDS)     # randomly choose correct answer
    guess = len(correct) * '-'  # state of guessing the word
    already_guessed = set()     # storing repetitive guesses

    while attempts > 0:
        print()
        print(guess)                       # printing the current state of the guessed word so far
        letter = input("Input a letter:")  # asking for a new letter

        # checking input
        if len(letter) != 1:
            print("Please, input a single letter.")
        elif letter not in ascii_lowercase:
            print("Please, enter a lowercase letter from the English alphabet.")
        else:
            if letter in already_guessed:
                print("You've already guessed this letter.")
            else:
                if letter in set(correct):
                    # replace - with the letter in the guess string and don't touch the rest of them
                    guess = "".join([x if x == letter
                                     else guess[correct.index(x)]
                                     for x in correct])
                else:
                    print("That letter doesn't appear in the word.")
                    attempts -= 1
            # if player inputs a letter, mark it as guessed to avoid repetitions
            already_guessed.add(letter)

        # GAME WON
        if guess == correct:
            print(f"You guessed the word {guess}!")
            print("You survived!")
            wins += 1
            return True
    # GAME OVER
    print()
    print("You lost!")
    loses += 1
    return False


# Main program
print("H A N G M A N")

while True:
    what_to_do = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if what_to_do == "exit":
        break
    elif what_to_do == "results":
        print(f"You won: {wins} times.")
        print(f"You lost: {loses} times.")
    elif what_to_do == "play":
        one_round()
    else:
        continue
