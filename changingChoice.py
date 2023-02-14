import random

"""
    Monty Hall problem
"""
def changing_choice(chosen_range):
    success_rate = 0
    
    for x in range(chosen_range):
        random_number = random.randint(1, 3) #Prize is behind this door
        guessed_number = random.randint(1, 3) #My first choice of door
        opened = 0
        print("Hidden prize is behind:", random_number, "I choose", guessed_number)
        if random_number != guessed_number: #Opens the losing door
            opened = 6-random_number-guessed_number
            print("Openes:", opened)
        else:
            if guessed_number == 1:
                opened = 2
                print("Openes:", opened)
            elif random_number == 2:
                opened = 3
                print("Openes:", opened)
            else:
                opened = 1
                print("Openes:", opened)
        
        changed_choice = 6-opened-guessed_number #I choose 3rd door (not my first choice and opened one)
        print("I change my choice to", changed_choice)

        if random_number == changed_choice:
            success_rate = success_rate + 1
            print("I succeeded")
        else:
            print("I failed")
    
    print("Success rate:", success_rate/chosen_range*100, success_rate, "from", chosen_range)

changing_choice(int(input("Input how many times to iterate ")))