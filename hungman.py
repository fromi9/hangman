import random

def hangman():
    print("Welcome to Hangman!")

    wordlist = ['tangerine', 'apple', 'pear', 'grape', 'orange', 'mango', 'mushroom', 'microphone', 'project', 'monitor', 'cross', 'fear']
    secret = random.choice(wordlist)
    guesses = ''
    attempts = 5

    while attempts > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end='')
            else:
                print('_', end=' ')
        missed += 1
        if missed == 0:
            print("You won!!!")
            break
        guess = input("Enter a letter: ")
        guesses += guess
        if guess not in secret:
            attempts -= 1
            print("Wrong guess.")
            print(f"Attempts left: {attempts}")
            if attempts < 5: print('  | ')
            if attempts < 4: print('  O ')
            if attempts < 3: print(' /|\ ')
            if attempts < 2: print('  | ')
            if attempts < 1: print(' / \ ')
        if attempts == 0:
            print("You lost!")

answer = "yes"
while answer.lower() == 'yes':
    hangman()
    ans = input("Do you want to play again? (yes or no)").strip().lower()
    if ans != 'yes':
        print("Thanks for game.")
        break
    
