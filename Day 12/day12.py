# # Namespaces: Local vs Global Scope
# # global 
# enemies = 1

# def increase_enemies():
#     # local
#     enemies = 2
#     print(f"enemies inside function : {enemies}")

# increase_enemies()
# print(f"enemies outside function : {enemies}")

# # There is no block scope in python
# game_level = 3
# enemies = ["skeleton", "zombies", "Alien"]

# if game_level < 5:
#     new_enemie = enemies[0]

# # this is give error if we put if part in function at that time it is act as local var only.
# print(new_enemie)

# Modifying Global Scope 
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function : {enemies}")

increase_enemies()
print(f"enemies outside function : {enemies}")