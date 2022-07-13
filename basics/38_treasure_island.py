print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("Where would you want to go? Right or left? ").lower()

if choice1 == 'left':
    choice2 = input('\nYou have come to a lake. There is an island in the middle of the lake.\nType "Wait" to wait for a boat. Type "Swim" to swim accross. ').lower()
    if choice2 == 'wait':
        choice3 = input("There is a house with three doors. One red, one yellow, and one blue.\nWhich colour do you choose?").lower()
        if choice3 == 'red':
            print("It's full of vampires. Game Over!")
        elif choice3 == 'yellow':
            print("Yellow is gold. You Win!")
        elif choice3 == 'blue':
            print("It's okay to feel blue but never choose blue. Game Over!") 
    else:
        print("You get attacked by a shark. Game Over.")
else:
    print("You fell into a hole. Game Over.")
