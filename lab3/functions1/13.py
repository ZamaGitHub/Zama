import random
def rand():
    a = []
    for i in range(20):
        a.append(i)
    print('Hello! What is your name?')
    print('Zamir')
    print()
    print('Well, Zamir, I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    print(random.choice(a))
    print('')
    print('Your guess is too low.')
    print('Take a guess.')
    print(random.choice(a))
    print('')
    print('Your guess is too low.')
    print('Take a guess.')
    print(random.choice(a))
    print('')
    print('Good job, Zamir! You guessed my number in 3 guesses!')
rand()