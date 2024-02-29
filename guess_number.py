number = 10
max_guesses = 3
remaining_guesses = max_guesses

print("I'm thinking of a number...")

while remaining_guesses > 0:
    guess = input("What number am I thinking of? (Enter 'q' to quit) ")
    
    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    
    guess = int(guess)
    
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
 limited-guesses
        print("Sorry! Your guess is too low.")
    else:
        print("Sorry! Your guess is too high.")
    
    remaining_guesses -= 1
    if remaining_guesses > 0:
        print(f"You have {remaining_guesses} guesses left.")
    else:
        print(f"Sorry! You've used all your guesses. The number was {number}.")

        print("Sorry! Your guess is too low. Try again.")
    else:
        print("Sorry! Your guess is too high. Try again.")
 main
