# necessary messages
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
messages = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
memory = 0  # use to store history of calculation


# check if input is float
def not_float(num):
    try:
        float(num)
        return False
    except ValueError:
        return True


# utility function to use later
def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    return False


# warn user not to perform simple calculation
def check(x, y, s):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and s == '*':
        msg += msg_7
    if (x == 0 or y == 0) and (s in ['*', '+', '-']):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


# main function to perform calculations
def calculator_1():
    global memory
    # checking input
    while True:
        print(msg_0)
        x, oper, y = input().split()
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        if not_float(x) or not_float(y):
            print(msg_1)
        elif oper not in ['+', '-', '*', '/']:
            print(msg_2)
        else:
            # performing calculations
            x = float(x)
            y = float(y)
            check(x, y, oper)
            if oper == '+':
                result = x + y
                break
            elif oper == '-':
                result = x - y
                break
            elif oper == '*':
                result = x * y
                break
            else:
                if y == 0:
                    print(msg_3)
                else:
                    result = x / y
                    break

    # printing result
    result = float(result)
    print(result)

    # store the result
    while True:
        print(msg_4)
        answer = input()
        if answer == 'y':
            # warn user not to store simple numbers
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(messages[msg_index])
                    sure = input()
                    if sure == 'y':
                        if msg_index < 12:
                            msg_index += 1
                        else:
                            memory = result  # store the result
                            break
                    elif sure == 'n':
                        break
                    else:
                        continue
                break
            else:
                memory = result
                break

        # if user doesn't answer yes to: do you want to store the result
        elif answer == 'n':
            break
        else:
            continue


# first iteration, after opening the app
calculator_1()

# continue calculations without restarting the app
while True:
    print(msg_5)
    cont = input()
    if cont == 'y':
        calculator_1()
    elif cont == 'n':
        break
    else:
        continue
