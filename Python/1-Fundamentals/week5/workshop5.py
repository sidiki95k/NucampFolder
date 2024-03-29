import random


def guess_random_number(tries, start, stop):
    target_number = random.randint(start, stop)

    while tries != 0:
        print(f"Tries remaining: {tries}")
        guess = int(input(f"Enter your guess (between {start} and {stop}): "))

        if guess == target_number:
            print("Congratulations! You guessed the correct number!")
            return
        elif guess < target_number:
            print("Guess higher!")
        else:
            print("Guess lower!")

        tries -= 1

    print(
        f"Sorry, you didn't guess correctly. The number was {target_number}.")


def guess_random_num_linear(tries, start, stop):
    target_number = random.randint(start, stop)

    print(f"Target number: {target_number}")

    for guess in range(start, stop + 1):
        print(f"Computer guesses: {guess}")
        if guess == target_number:
            print("Congratulations! The computer guessed the correct number!")
            return
        tries -= 1
        if tries == 0:
            break

    print("Sorry, the computer couldn't guess the number.")


def guess_random_num_binary(tries, start, stop):
    target_number = random.randint(start, stop)

    print(f"Target number: {target_number}")

    left, right = start, stop

    while left <= right and tries > 0:
        mid = (left + right) // 2
        print(f"Computer guesses: {mid}")

        if mid == target_number:
            print("Congratulations! The computer guessed the correct number!")
            return

        if mid < target_number:
            left = mid + 1
        else:
            right = mid - 1

        tries -= 1

    print("Sorry, the computer couldn't guess the number.")

# Test Task 1
# guess_random_number(5, 0, 10)

# Test Task 2
# guess_random_num_linear(5, 0, 10)


# Test Task 3
guess_random_num_binary(5, 0, 100)
