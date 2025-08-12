# battlegame.py

# -----------------------------------
# Game Setup
# -----------------------------------

# Characters
wizard = "Wizard"
elf = "Elf"
human = "Human"

# Health Points
wizard_hp = 70
elf_hp = 100
human_hp = 150

# Damage
wizard_damage = 150
elf_damage = 100
human_damage = 20

# Dragon stats
dragon_hp = 300
dragon_damage = 50

# Character Selection
while True:
    print("Choose your character:")
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")

    character_choice = input("Select your character: ")

    if character_choice == "1":
        char = wizard
        player_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character_choice == "2":
        char = elf
        player_hp = elf_hp
        my_damage = elf_damage
        break
    elif character_choice == "3":
        char = human
        player_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Invalid choice. Please try again.\n")

print(f"\nYou have chosen the {char}!\n")

# -----------------------------------
# Battle with the Dragon
# -----------------------------------
while True:
    # Player's turn
    dragon_hp = dragon_hp - my_damage
    print(f"The {char} damaged the Dragon!")
    print(f"Dragon's HP is now: {dragon_hp}")

    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break

    # Dragon's turn
    player_hp = player_hp - dragon_damage
    print(f"The Dragon damaged the {char}!")
    print(f"{char}'s HP is now: {player_hp}\n")

    if player_hp <= 0:
        print(f"The {char} has lost the battle!")
        break
