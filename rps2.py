import random
def choose_random():
    return random.randint(0,2)

def check_win(input_1,input_2):
    diff = input_1 - input_2

    if diff == 0:
        return "Tie!"
    elif diff == -1 or diff == 2:
        return "Loss"
    elif diff == -2 or diff == 1:
        return "Win!"
    else:
        return "Uh Oh"
    


def get_user_input():
    valid_input = False
    while not valid_input:
        user_input = input("Rock(0), Papeer(1), or Scissors(2). (Q) to quit: ")
        if user_input == "Q":
            return user_input
        if user_input == "0" or user_input =="1" or user_input =="2" or user_input =="Q":
            valid_input = True
            return int(user_input)
        else:
            print("invalid input!")

game_going = True

options = ["Rock", "Paper", "Scissors"]

while game_going:
    user_input = get_user_input()
    if user_input == "Q":
        break

    computer_input = choose_random()
    print(f"you chose: {options[user_input]}")
    print(f"computer chose: {options[computer_input]}")
    print(check_win(user_input, computer_input))