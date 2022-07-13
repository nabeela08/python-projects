# local scopes 
from turtle import position

# local scope 
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(position_strength) #we can't access it here outside the function

# global scope 
player_health = 10 #global variable

def drink_potion():
    potion_strength = 2
    print(potion_strength) #local 

drink_potion()

