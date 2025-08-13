import random
print("Welcome to 'whose wallet?'")
print("You will give me a list of names and I will randomly select one to pay")
names=input("If you are ready, enter the names separated by a comma ,,, \n ").split(",")
names = [name.strip() for name in names if name.strip()]
if names:
  print("The person who will pay is: ", random.choice(names))
else:
  print("You did not enter any names, please try again")
print("thanks for playing 'whose wallet?'")