import random

"""
    Chooses ramdnom number from 1 to 3
"""
def choosing_random_number():
    randomNumber = random.randint(1, 3)
    choice_text = "My Choice from 1 to 3 is {} "
    print(choice_text.format(randomNumber))

"""
    Chooses random number n times and counts their frequency
"""
def choosing_random_numbers(interation_times):
    
    ones = 0
    twos = 0
    threes = 0

    for x in range(interation_times):

        number1 = random.randint(1, 3)
        print("Random number is ", number1)
        
        if number1 == 1:
            ones = ones + 1
        elif number1 == 2:
            twos = twos + 1
        else:
            threes = threes + 1
    
    print("1:", ones, " 2:", twos,  " 3:", threes)

choosing_random_number()
choosing_random_numbers(100)