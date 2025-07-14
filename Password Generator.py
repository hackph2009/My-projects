import string
import random
print("   *** Welcome to the Password Generator! ***   ")
password_length = int(input("Enter the length of the password: "))
print("------------------------------------------------\n")
letter=int(input("Enter the letter you want to include in the password: "))
print("------------------------------------------------\n")
numbers=int(input("Enter the numbers you want to include in the password: "))
print("------------------------------------------------\n")
sympols=int(input("Enter the symbols you want to include in the password: "))
print("------------------------------------------------\n")
#validation
if password_length < letter + numbers + sympols:
    print("The length of the password is too short for the number of letters, numbers and symbols you want to include.")
elif password_length > letter + numbers + sympols:
    print("The length of the password is too long for the number of letters, numbers and symbols you want to include.")
elif password_length == letter + numbers + sympols:
    #continue validation with the password generator
    password = []
    password.extend(random.choices(string.ascii_letters, k=letter))
    password.extend(random.choices(string.digits, k=numbers))
    password.extend(random.choices(string.punctuation, k=sympols))
    random.shuffle(password)
    print("👇👇👇 Your password is: 👇👇👇")
    print("".join(password))
else:
    print("Please the input is empty or invalid.")







