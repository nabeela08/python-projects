scores = input("Input a list of numbers ").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])
print(scores)

highest_score = 0
for score in scores:
    if score>highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
