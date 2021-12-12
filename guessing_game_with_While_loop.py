#Exercise for guessing game

secret_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
   guess = int(input("Guess: "))
   guess_count += 1
   if guess==secret_number:
       print(f"You win my boy! the secret number is {secret_number}")
       break

else:
    print("You lose boy! You already tried three times")