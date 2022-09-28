import random 
number = random.randint(0,100) #Chooses a number from 1 to 100
guess = ''
guess_count = 0 
guess_limit = 8 #Number of Guesses you have
guesses_gone = False

print('Welcome to the number guessing game')
a = input('Enter your name')
print('Welcome to the game',a)


while guess != number and not(guesses_gone): #Checks whether guesses are gone or not
    if guess_limit > guess_count: #Checks whether the guesses are available or not
        guess = int(input('What\'s your guess(1-100)'))
        if guess > number:
            print('The number is lesser')
        elif guess < number:
            print('The number is greater')
        guess_count += 1 #Increases guess count
    else:
        guesses_gone = True #Guesses are over

if guesses_gone == True: 
    print('You lost')
else:
    print('You win!')
