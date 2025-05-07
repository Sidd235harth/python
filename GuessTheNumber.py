import random
print(" Siddarth TR \n USN:1AY24AI106 \n sec:o")
# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

# Let the user guess up to 6 times
for guesses_taken in range(1, 7):
    guess = int(input("Take a guess.\n"))
    
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        break  # Correct guess!

if guess == secret_number:
    print(f"Good job! You guessed my number in {guesses_taken} guesses!")
else:
    print(f"Nope. The number I was thinking of was {secret_number}.")
