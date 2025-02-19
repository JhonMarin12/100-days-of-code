from treasure import treasure

print(treasure)
print("Welcome to Treasure Island.")
print("Your mission es to find the treasure.")
print("You're at cross road. Where do you want to go?")
option =  input('Type "left" or "right\n')

if option == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    option =  input('Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if option == 'swim':
        print("You get attacked by an angry trout. Game Over.")
    elif option == 'wait':
        print('You arrive at the island unharmed. There is a house with 3 doors.')
        option = input('One red, one yellow and one blue. Which colour do you choose?\n')
        if option == 'red':
            print("It's a room full of fire. Game Over.")
        elif option == 'yellow':
            print("You found the treasure! You Win!")
        elif option == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("Not valid option")
    else:
        print("Not valid option")
elif option == 'right':
    print('You fell into a hole. Game Over.')
else:
    print("Not valid option")
