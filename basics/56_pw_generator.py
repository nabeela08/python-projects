#Password Generator Project
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the Password Generator!")
n_letters = int(input("How many letters you want in your password?\n"))
n_numbers = int(input("How many numbers you want in your password?\n"))
n_symbols = int(input("How many symbols you want in your password?\n"))

#Easy level
# pw = ""

# for char in range(1, n_letters+1):
#     pw += random.choice(letters)

# for char in range(1, n_numbers+1):
#     pw += random.choice(numbers)

# for char in range(1, n_symbols+1):
#     pw += random.choice(symbols)

# print(pw)

#Hard level
pw_list = []

for char in range(1, n_letters+1):
    pw_list += random.choice(letters)

for char in range(1, n_numbers+1):
    pw_list += random.choice(numbers)

for char in range(1, n_symbols+1):
    pw_list += random.choice(symbols)

# print(pw_list)
random.shuffle(pw_list)
# print(pw_list)

pw = ""
for char in pw_list:
    pw += char

print(f"\nYour password is: {pw}")
