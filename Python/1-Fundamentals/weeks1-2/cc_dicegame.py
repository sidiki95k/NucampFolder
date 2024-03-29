import random

high_score = 0

def dice_game():
    global high_score

    print("Welcome to the Dice Game!")

    while True:
        print("\nOptions:")
        print("1. Roll the dice")
        print("2. Quit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            total = dice1 + dice2

            print(f"\nYou rolled: {dice1} + {dice2} = {total}")

            if total == 7:
                print("You rolled a 7!")
                if total > high_score:
                    high_score = total
                    print(f"New high score: {high_score}")
            else:
                print("Current total:", total)
        elif choice == '2':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


