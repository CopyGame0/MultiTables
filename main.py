import os
import random
import options

Pscore = 100

inputs = None

clear = lambda: os.system('cls')


def origin():
    global inputs

    print("Multiplication tables ")
    print("")

    try:
        print("Select a multiplication table with the number (for practice 0)")
        inputs = int(input(""))
    except Exception:
        print("something went wrong :(")
        print("")
        origin()

    if inputs == 0:

        clear()
        practice()

    else:
        options.options(inputs)

    print("End program y/n ")
    end_question = input("")

    if end_question == "y":
        return
    else:

        clear()
        origin()


def practice():
    global Pscore

    x = random.randint(1, 10)
    y = random.randint(1, 10)

    z = x * y

    user_gues = int(input(str(x) + " * " + str(y) + " = "))

    print("")

    if user_gues == z:
        Pscore = Pscore + 10

        print("congratulations your answer was right ")
        print("+10 points, total = ", Pscore)
        print("")
        print("")

    else:
        Pscore = Pscore - 5

        print("No, the answer was ", z)
        print("Do better in the next. -5 points, total = ", Pscore)
        print("")
        print("")

    print("again y/n")

    end_question = input("")

    if end_question == "n":

        clear()
        return

    else:

        clear()
        practice()


origin()
