import random

letters = 'abcdefghijklmnopqrstuvwxyz'
largeLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
specialCharacters = "!@#$%^&*()_+-={}[]:\"|;'\,./<>?`~|"

chars = letters + largeLetters + digits + specialCharacters

def genPassword(n):
    password = ''
    for i in range(1,n+1):
        password += chars[random.randint(0,len(chars)-1)]
    return password

while True:
    max = input("How long should the password be? (10 chars minimum): ")
    if not max.isdigit():    
        print('Provided value cannot be convetred to a integer.\n')
    elif not int(max) >= 10:
        print('Not enough characters.\n')
    else:
        print(genPassword(int(max)))
        break