height = int(input("Enter height in cm : "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("\nWhat is your age? "))
    if age<12:
        bill = 5
        print('Child tickets are ₹5.')
    elif age<=18:
        bill = 7
        print('Youth tickets are ₹7.')
    else:
        bill = 12
        print('Adult tickets are ₹12.')

    wants_photo = input('Do you want a photo taken? Y or N. ')
    if wants_photo == 'Y':
        bill += 3
    print(f'Your final bill is ₹{bill}.')
else:
    print('You have to grow taller.')

print()