import random

def Computer_guess(x):
    low = 1
    high = x
    feedback= ''

    while feedback != 'c':
        if low !=high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f'(is {guess} too high(H), too low (L), Or correct guess (C))').lower 
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess + 1
    print("Awesome Guess ")

  
Computer_guess(100) 

# maximum