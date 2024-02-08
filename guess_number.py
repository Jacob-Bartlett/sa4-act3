number = 10

print("I'm thinking of a number...")

guess_cap = 10
y_q = "Y"

while y_q == "Y":
    if y_q == "Q":
        print(f"Sorry! The number was {number}.")
        break
    guess = int(input("What number am I thinking of? "))
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess != number:
        guess_cap -= 1
        print(f"You have {guess_cap} guesses left.")
        if guess > number:
            print("Guess lower!")
        else:
            print("Guess higher!")
    elif guess_cap == 0:
        print("You ran out of guesses!")
        break
    y_q = input("Try again? (Y) or Quit? (Q) ")
