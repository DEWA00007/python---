# Encryption program::

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

message= input("Enter the message to encrypt: ")
encrypt = ""
for letter in message: 
    index = chars.index(letter)
    encrypt += key[index]
print(f"The encrypted message is: {encrypt}")    

decrypt = ""
for letter in encrypt :
    index = key.index(letter)
    decrypt += chars[index]
print(f"The decrypted message is: {decrypt}")       