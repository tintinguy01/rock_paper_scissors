import random

# VARIABLES
choice_list = ['rock', 'paper', 'scissors']
count_win = 0
count_lose = 0
count_draw = 0

# PLAYING
while True:

    # QUIT?
    exit = input(
        'Do you want to quit this game? If you want to quit press Q for quit: ').lower()
    if exit == 'q':
        break

    # USER CHOICE
    user_choice = input("Please input your choice: ").lower()

    # CHECK
    if user_choice in choice_list:
        print("You choose " + user_choice)

        computer_choice = random.choice(choice_list)
        print("Computer choose: " + computer_choice)

        # CALCULATING
        if user_choice == computer_choice:
            print("Result: Draw")
            count_draw += 1

        if user_choice == 'rock' and computer_choice == 'scissors':
            print("Result: Win")
            count_win += 1

        if user_choice == 'paper' and computer_choice == 'rock':
            print("Result: Win")
            count_win += 1

        if user_choice == 'scissors' and computer_choice == 'paper':
            print("Result: Win")
            count_win += 1

        else:
            print("Result: Lose")
            count_lose += 1

    else:
        print('Please select rock, paper, or scissors')
        continue

# RESULT
print("Result: Win: " + str(count_win) + " win" + "\nLose: " +
      str(count_lose) + " lose" + "\nDraw: " + str(count_draw) + " draw")
print('Thanks for playing!!')
