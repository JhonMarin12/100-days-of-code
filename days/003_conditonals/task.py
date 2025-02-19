## Task: Write a program that asks the user for their height in cm. If they are over 120cm, print "You are tall enough to ride!", otherwise print "You are not tall enough to ride!"

height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))

if height >= 120:
    print("You are tall enough to ride!")
    if age < 12:
        bill = 12
        print("your ticket price is $5")
    elif age <= 18:
        bill = 7
        print("Your ticket price is $7")
    else:
        bill = 12
        print("Your ticket price is $12")

    wants_photo = input("Do you want a photo? (yes/no) ")
    if wants_photo == "yes":
        print("Photo price is $3")
        bill += 3
    else:
        print("No photo")
    print(f"Your total bill is ${bill}")
else:
    print("You are not tall enough to ride!")

## write a program to check if a number is even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Number is even")
else:  
    print("Number is odd")


## pizza order program
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").capitalize()
add_pepperoni = input("Do you want pepperoni? Y or N ").capitalize()
extra_cheese = input("Do you want extra cheese? Y or N ").capitalize()
bill = 0

# todo: work out how much the pizza will cost based on the size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size")

# todo: work out how much the pizza will cost based on their pepperoni addition.
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out how much the pizza will cost based on their extra cheese addition.
if extra_cheese == "Y":
    bill += 1

# todo: print the final bill
print(f"Your final bill is: ${bill}")
