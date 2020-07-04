
import random
import string

def generate_nomen(length=32, uppercase=True, lowercase=True, numbers=True):
    character_set = ''
    if uppercase:
        character_set += string.ascii_uppercase
    if lowercase:
        character_set += string.ascii_lowercase
    if numbers:
        character_set += string.digits       
    
    return ''.join(random.choice(character_set) for i in range(length))

print("Press enter to generate or press any other key to exit...")

while True:
    if input() == '':
        nomen = generate_nomen(length=5, uppercase=True, lowercase=False, numbers=False)
        print(nomen)
    else:
        break