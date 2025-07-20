import random
print("Welcome to the coin flip game!")
print("choose a method to toss a coin")
print("1. Using random.random()")
print("2. Using random.randint()")
method = input("Enter your choice (1 or 2): \n ")
if method == "1":
  guess = input("Enter your guess (heads or tails): \n ").lower()
  coin = random.random()
  if coin < 0.5:
    result = "heads"
    if guess == result:
      print("You win! The coin landed on heads.")
    elif guess != "tails" and guess != "heads":
      print("Invalid guess, please choose either heads or tails.")
    else:
      print("You lose! The coin landed on heads.")
  else:
    result = "tails"
    if guess == result:
      print("You win! The coin landed on tails.")
    elif guess != "tails" and guess != "heads":
      print("Invalid guess, please choose either heads or tails.")
    else:
      print("You lose! The coin landed on tails.")
elif method == "2":
  guess = input("Enter your guess (heads or tails): \n ").lower()
  coin = random.randint(0, 1)
  if coin == 0:
    result = "heads"
    if guess == result:
      print("You win! The coin landed on heads.")
    elif guess != "tails" and guess != "heads":
      print("Invalid guess, please choose either heads or tails.")
    else:
      print("You lose! The coin landed on heads.")
  else:
    result = "tails"
    if guess == result:
      print("You win! The coin landed on tails.")
    elif guess != "tails" and guess != "heads":
      print("Invalid guess, please choose either heads or tails.")
    else:
      print("You lose! The coin landed on tails.")
else:
  print("Invalid choice, please try again.")
