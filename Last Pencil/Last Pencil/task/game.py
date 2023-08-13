from random import randint

players = ["John", "Jack"]

num = input("How many pencils would you like to use:")

while True:
    if not num.isnumeric():
        print("The number of pencils should be numeric")
    elif int(num) < 0:
        print("The number of pencils should be numeric")
    elif int(num) == 0:
        print("The number of pencils should be positive")
    else:
        num = int(num)
        break
    num = input()

name = input("Who will be the first (John, Jack):")

while name not in players:
    print("Choose between 'John' and 'Jack'")
    name = input()

print(num * '|')

if name == "John":
    i = 0
else:
    i = 1

while True:
    print(players[i % 2], "'s turn:")
    if i % 2 == 0:
        n = input()
        going = True

        while going:
            if n not in ['1', '2', '3']:
                print("Possible values: '1', '2' or '3'")
                n = input()
            elif num - int(n) < 0:
                print("Too many pencils were taken")
                n = input()
            else:
                n = int(n)
                going = False
    else:
        if num % 4 == 1 and num != 1:
            n = randint(1, 3)
        elif num == 1:
            n = 1
        else:
            n = (num % 4 + 3) % 4
        print(n)

    num -= n
    if num == 0:
        print(players[(i % 2 + 1) % 2], "won!")
        break
    else:
        print(num * '|')
        i += 1
