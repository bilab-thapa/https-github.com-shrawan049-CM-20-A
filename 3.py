import random
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
passlen = 8
password = ''
for c in range (8):
    password += random.choice(characters)
print(password)



