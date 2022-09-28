import random
number = random.randint(0,100)
guess = ''
guess_count = 0
guess_limit = 8
guesses_gone = False

print('Welcome to the number guessing game')
a = input('Enter your name')
print('Welcome to the game',a)


while guess != number and not(guesses_gone):
    if guess_limit > guess_count:
        guess = int(input('What\'s your guess(1-100)'))
        if guess > number:
            print('The number is lesser')
        elif guess < number:
            print('The number is greater')
        guess_count += 1
    else:
        guesses_gone = True

if guesses_gone == True:
    print('You lost')
else:
    print('You win!')
