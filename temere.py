
import random
import string

def generate_temere(length=32, uppercase=True, lowercase=True, numbers=True):
    
    character_set = ''
    
    if uppercase:
        character_set += string.ascii_uppercase
    if lowercase:
        character_set += string.ascii_lowercase
    if numbers:
        character_set += string.digits       
    
    return ''.join(random.choice(character_set) for i in range(length))


user_letter = input("Please select a letter: ")

print("Press enter to generate...")

while True:
    if input() == '':
        result = generate_temere(4, True, False, False)
        print(user_letter + result)
    else:
        break