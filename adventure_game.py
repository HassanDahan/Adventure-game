import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
    return response


def intro(enemy):
    print_pause("You find yourself standing in an open field, filled with"
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, and"
                " has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.")


def house(enemy, weapon, items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out "
                f"steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    if weapon not in items:
        print_pause("You feel a bit under-prepared for this, what with only"
                    "having a tiny dagger.")

    door_choice = input("Would you like to (1) fight or (2) run away?")

    if door_choice == "1":
        fight(enemy, weapon, items)
    elif door_choice == "2":
        print_pause("You run back into the field. Luckily, you don't seem to "
                    "have been followed.")
        field(enemy, weapon, items)


def cave(enemy, weapon, items):
    if weapon not in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical {weapon} of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    f"the {weapon} with you.")
        print_pause("You walk back out to the field.")
        items.append(weapon)
        field(enemy, weapon, items)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field(enemy, weapon, items)


def fight(enemy, weapon, items):
    if weapon not in items:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {enemy}.")
        print_pause("You have been defeated!")
    else:
        print_pause(f"As the {enemy} moves to attack, you unsheath "
                    f"your new {weapon}.")
        print_pause(f"The {weapon} of Ogoroth shines brightly in your hand as "
                    "you brace yourself for the attack.")
        print_pause(f"But the {enemy} takes one look at your shiny "
                    "new toy and runs away!")
        print_pause(f"You have rid the town of the {enemy}. "
                    "You are victorious!")
        items.clear()


def field(enemy, weapon, items):
    print_pause("\n"
                "Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    choice = valid_input("(Please enter 1 or 2).\n", "1", "2")

    if choice == "1":
        house(enemy, weapon, items)
    elif choice == "2":
        cave(enemy, weapon, items)


def play_again():
    play_again = valid_input("Would you like to play again? (y/n)", "y", "n")

    if play_again == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif play_again == "n":
        print_pause("Thanks for playing! See you next time.")


def play_game():
    enemy = random.choice(["troll", "dragon", "wicked fairie", "giant",
                          "gorilla", "pirate", "gorgon"])
    weapon = random.choice(["Sward", "Hammer", "Cross & Bow"])
    items = []
    intro(enemy)
    field(enemy, weapon, items)
    play_again()


play_game()
