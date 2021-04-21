import random

print("Number guessing game")
number = random.randint(1,9)
game = 0
print("Guess the number between 1 and 9")

while game < 5:
    guess = int(input("Enter your guess: \n"))
    if guess == number:
        print("Congratulations!! You won!")
        break
    elif guess < number:
        print("Your guess was too low. Guess a higher number", guess)
    else:
        print("Your guess was too high please pick a lower number", guess)
    game += 1
if not game < 5:
    print("You lose. The number is", number)
