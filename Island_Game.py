print("""
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
   """)
print("Welcome to my island!🏝️🏝️")
print("There is 3 doors🚪 in front of you, Red door🚪, Blue door🚪, Yellow door🚪")
door=input("Which door would you like to enter🤔🤔?").lower()
if door == "red":
 print("Great😁! You have entered the true door🙌!")
 box=input("Now you have to choose white box⬜ or black box⬛ or green box🟩: \n").lower()
 if box == "white":
   print("Congratulations🎉! You have won the game🙌🥳!")
 elif box == "black" or box == "green":
   print("Oops😥 you have eaten by a monster👹👻!")
 else:
    print(f"The input {box} is not valid🤨🤷‍♂️🤷‍♂️")
elif door == "blue" or door== "yellow":
 print("Oops😥 you have entered a fire🔥🔥!")
else:
 print(f"The input {door} is not valid🤨🤷‍♂️🤷‍♂️")