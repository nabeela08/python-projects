enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemeies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
