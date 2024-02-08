number = 10

print("I'm thinking of a number...")
guess = -999999999

guess_cap = 10

while guess != number:
    guess = (input("What number am I thinking of? (Press q to quit) "))
    if guess == "q":
        print(f"Sorry! The number was {number}.")
        break
    elif guess == number:
        print("Congratulations! You guessed the right number.")
    elif guess != number:
        guess_cap -= 1
        if guess_cap == 0:
            print("You ran out of guesses!")
            break
        else:
            print(f"You have {guess_cap} guesses left.")
        print("Try again!")