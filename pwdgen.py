import random
print("Welcome to your Password Generator")
chars = 'abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = input('Amount of password to generate: ')
number = int(number)
length = input('Input your password length: ')
length = int(length)
print('\nHere are your passwords: ')
for pwd in range(number):
    passwords = ' '
    for c in range(length):
        password += random.choice(chars)
        print(passwords)
