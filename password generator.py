import random 
import string 

def password_generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

length = (input("Enter the length of your password: "))

if length.isdigit():
    print("Generated password is: ", password_generate(int(length)))
else:
    print("Invalid text please enter a digit! ")
             