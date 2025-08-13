import random 
group=["red", "blue", "pink", "yellow", "green"]
random_word=random.choice(group)
display=len(random_word)*"_".split()
print(" ".join(display), "\n")
chances=6
blocked=[]
ascii_draw=['''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',''' 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
while "_" in display and chances>0:
    guess=input("Please guess a letter: ").lower()
    if guess not in random_word:
        if guess not in blocked:
            chances-=1
            blocked.append(guess)
            for x in range(6):
                if x ==chances:
                    print(ascii_draw[x])
                    break
        print("You already guessed that. Try again")
        print(f"You have {chances} left")
    for position in range(len(random_word)):
        if  random_word[position] ==guess and guess not in display[position]:
            display[position]=guess
            break
    print("\n"," ".join(display), "\n")
    print(f"You have {chances} more chances")
    print("---------------\n")
if chances==0:
    print("""
YOU LOSE!
""")    
    print("""
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""")
else:
    print("""
~~~~~~~~~~~~~~
***YOU WIN!***
~~~~~~~~~~~~~~          
""")