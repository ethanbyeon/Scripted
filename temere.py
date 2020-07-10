
import random
import string

from itertools import permutations

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


def permutate(string):

    # letters = list(string)
    
    # for i in range(0, len(letters) + 1):
    #     for subset in itertools.combinations(letters, i):
    #         print(subset)

    word, n = string.split()
    print(*[''.join(i) for i in permutations(sorted(word), int(n))], sep='\n')


select_msg = f"""
{'-'*40}
Please select one of the following functions:

(t) TEMERE
(s) SCRAMBLE 
(p) PERMUTATE

{'-'*40}
"""

option_msg = "YES ('True') | NO ('False'): "

while True:

    user_select = input(select_msg)

    if user_select not in ['t', 's', 'p']:
        print("Please enter a valid function.\n")
        continue

    if user_select == 't':

        string_length = int(input("Please enter a length for string: "))
        caps = input("Inclue uppercase? " + option_msg)
        lows = input("Include lowercase? " + option_msg)
        numbers = input("Include numbers? "+ option_msg)
        print("Press enter to generate and q to stop...")

        while True:
            if input() != 'q':
                result = generate_temere(string_length, caps, lows, numbers)
                print(result)
            else:
                break

    if user_select == 's':

        user_input = input("Please enter a string to randomize: ")
        print("Press enter to generate and q to stop...")
        
        while True:
            if input() != 'q':
                result = scramble(user_input)
                print(result)
            else:
                break

    if user_select == 'p':
        user_input = input("Please enter a string and length (Ex. ANDY 2): ")
        permutate(user_input)

    print('-'*40)
    ask_continue = input("Would you like to continue? (Yes or No): ").upper()
    if ask_continue == "Y" or ask_continue == "YES":
        continue
    else:
        break
