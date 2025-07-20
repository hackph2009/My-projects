import random
Guess=int(input("Guess a number between 1 and 10: " ))
number=random.randint(1,10)
while Guess != number:
  if Guess < number:
    print("Your guess is too low.👆⬆️\n")
    print("---------------------\n")
    Guess=int(input("Guess a number between 1 and 10: " ))
  else :
    print("Your guess is too high.👇⬇️🔽\n")
    print("---------------------\n")
    Guess=int(input("Guess a number between 1 and 10: " ))
print("------🙌🥳🎉🎊Congratulations! You guessed the number.🙌🥳🎉🎊------")