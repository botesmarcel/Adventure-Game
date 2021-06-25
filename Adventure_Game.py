import time
import random

items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


monsters = ["fairy", "pirate", "dragon", "vampire", "witch"]
weapons = ["sword", "machine gun", "nunchucks"]


def play_again(prompt, y, n):
    while True:
        response = input('Would you like to play again? (y/n)')
        if response == 'y':
            global items
            items = []
            main()
        elif response == 'n':
            print_pause("Thanks for playing! See you next time")
            exit()
        else:
            print_pause("Please enter y or n")


def choices():
    while True:
        choice = input("(Please enter 1 or 2.)")
        if choice == "1":
            house()
        elif choice == "2":
            cave()
        else:
            print("Please try again")


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when"
                f" the door opens and out steps a {monster}.")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    if 'weapon' in items:
        print_pause(f"As the {monster} moves"
                    " to attack,"
                    f" you unsheath your new {weapon}")
        print_pause(f"The {weapon} of Ogoroth shines brightly in your hand"
                    " as you brace yourself for the attack.")
        print_pause(f"But the {monster} takes one look"
                    " at your shiny new toy"
                    " and runs away!")
        print_pause(f"You have rid the town of the {monster}."
                    " You are victorious!")
        while True:
            response = play_again("Would you like to play again?"
                                  " (y/n)", "y", "n")
            if "y" in response:
                main()
            elif "n" in response:
                print_pause("Thanks for playing! See you next time")

    else:
        print_pause("You feel a bit under-prepared for this,"
                    " what with you only having a tiny dagger.")
        choice = input("(Would you like to (1) fight of (2) run away?)")
        if choice == '1':
            print_pause("You do your best...")
            print_pause("but your dagger is no match"
                        f" for the {monster}.")
            print_pause("you have been defeated!")
            while True:
                response = play_again("Would you like to play again?"
                                      " (y/n)", "y", "n")
                if "y" in response:
                    main()
                elif "n" in response:
                    print_pause("Thanks for playing! See you next time")
                    exit()

        elif choice == '2':
            print_pause("You run back into the field."
                        " Luckily, you don't seem to have been followed.\n")
            print_pause("Enter 1 to knock on the door of the house.")
            print_pause("Enter 2 to peer into the cave.")
            print_pause("What would you like to do?")


def cave():
    print_pause("You peer cautiosly into the cave.")
    if 'weapon' in items:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical {weapon} of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        items.append('weapon')

    print_pause("You walk back out to the field\n")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    choices()


def main():
    global monster, weapon
    monster = random.choice(monsters)
    weapon = random.choice(weapons)
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a wicked {monster} is"
                " somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you there is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    choices()


main()
