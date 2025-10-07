import hands
from random import randint

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
options = [hands.rock, hands.paper, hands.scisors]
pc_option = randint(0, 2)
user_option = int(input("Choose your option: "))

if pc_option == user_option:
    print("Draw")
elif (pc_option == 0 and user_option == 1 or
    pc_option == 1 and user_option == 2 or
    pc_option == 2 and user_option == 0):
    print("Computer option:")
    print(options[pc_option])
    print("Your option:")
    print(options[user_option])
    print("You win")
else:
    print("Computer option:")
    print(options[pc_option])
    print("Your option:")
    print(options[user_option])
    print("You lose")


# This code use multiple nested conditional, but the idea is not repeat yourself, so the solution use logical operator that evaluate the cases when the user wins/loses.
# if pc_option == user_option:
#     print("Computer option")
#     print(options[pc_option])
#     print("Your option")
#     print(options[user_option])
#     print("Draw")
# elif pc_option == 0:
#     print("Computer option")
#     print(options[pc_option])
#     if user_option == 1:
#         print("Your option")
#         print(options[user_option])
#         print("You win")
#     else:
#         print("Your option")
#         print(options[user_option])
#         print("You lose")
# elif pc_option == 1:
#     print("Computer option")
#     print(options[pc_option])
#     if user_option == 2:
#         print("Your option")
#         print(options[user_option])
#         print("You win")
#     else:
#         print("Your option")
#         print(options[user_option])
#         print("You lose")
# else:
#     print("Computer option")
#     print(options[pc_option])
#     if user_option == 1:
#         print("Your option")
#         print(options[user_option])
#         print("You lose")
#     else:
#         print("Your option")
#         print(options[user_option])
#         print("You win")
