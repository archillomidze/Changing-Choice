import random

"""
    Chooses randomly from 1 to 3 twice and counts how requent was coincidence from inputed times
"""
def guessing_number(chosen_range):

    success_rate = 0

    for x in range(chosen_range):
        random_number = random.randint(1, 3)
        guessed_number = random.randint(1, 3)
        print(random_number, "then", guessed_number)
        if random_number == guessed_number:
            success_rate = success_rate + 1
    
    print("Success rate", success_rate, "from", chosen_range)

guessing_number(int(input("Input how many times to iterate ")))
