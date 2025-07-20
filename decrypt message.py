import string
def decrypt(message, password):
    alphabet=string.ascii_lowercase
    decrypted_word= ""
    for letter in message:
        if letter.lower()in alphabet:
            position=alphabet.index(letter.lower())
            new_word=alphabet[(position-password)%26]
            if letter.isupper():
                decrypted_word+=new_word.upper()
            else:
                decrypted_word+=new_word
        else:
           decrypted_word += letter
    print("Here is your original message ",decrypted_word )
word=input("Please enter a message: ")
shift_key=int(input("Please enter a shift key (Password): "))
decrypt(word, shift_key)