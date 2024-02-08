number = 10

print("I'm thinking of a number...")
guess = -999999999


while guess != number:
    guess = (input("What number am I thinking of? (Press q to quit) "))
    if guess == "q":
        print(f"Sorry! The number was {number}.")
        break
    elif guess == number:
        print("Congratulations! You guessed the right number.")
    elif guess != number:
        print("Try again!")