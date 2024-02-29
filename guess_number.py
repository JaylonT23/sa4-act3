number = 10

print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? (Enter 'q' to quit) ")
    
    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    
    guess = int(guess)
    
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Sorry! Your guess is too low. Try again.")
    else:
        print("Sorry! Your guess is too high. Try again.")
