import string
def encrypt(message, password):
    alphabet=string.ascii_lowercase
    encrypted_word= ""
    for letter in message:
        if letter.lower()in alphabet:
            position=alphabet.index(letter.lower())
            new_word=alphabet[(position+password)%26]
            if letter.isupper():
                encrypted_word+=new_word.upper()
            else:
                encrypted_word+=new_word
        else:
           encrypted_word += letter
    print("Here is your encrypted word ",encrypted_word )
word=input("Please enter a message: ")
shift_key=int(input("Please enter a shift key (Password): "))
encrypt(word, shift_key)