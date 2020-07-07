
import random
import string
import itertools

def generate_temere(length=32, uppercase=True, lowercase=True, numbers=True):
    
    character_set = ''
    
    if uppercase:
        character_set += string.ascii_uppercase
    if lowercase:
        character_set += string.ascii_lowercase
    if numbers:
        character_set += string.digits       
    
    return ''.join(random.choice(character_set) for i in range(length))

def scramble(word):

    jumble = ''

    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    
    return jumble


def permutations(string):
    
    for i in range(0, len(list) + 1):
        for subset in itertools.combinations(list, i):
            print(subset)


# user_letter = input("Please select a letter: ")
user_word = input("Please enter a word: ")

print("Press enter to generate...")

while True:
    if input() == '':
        # result = generate_temere(4, True, False, False)
        # print(user_letter + result)

        result = scramble(user_word)
        print(result)
    else:
        break