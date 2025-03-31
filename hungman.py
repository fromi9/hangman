import random

def hangman():
    print("Добро пожаловать в Виселицу.")

    wordlist = ['мандарин', 'яблоко', 'груша', 'виноград', 'апельсин', 'манго', 'гриб', 'микрофон', 'проект', 'монитор', 'крест', 'страх']
    secret = random.choice(wordlist)
    guesses = ''
    turns = 5

    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                missed += 1
        print()

        if missed == 0:
            print("Ты выиграл!!!")
            return
        
        guess = input("Напиши букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, вводи только одну букву!")
            continue

        if guess in guesses:
            print("Ты уже называл эту букву.")
            continue

        guesses += guess

        if guess not in secret:
            turns -= 1
            print("Не угадал.")
            print(f"Осталось {turns} попыток")
            if turns < 5: print("  | ")
            if turns < 4: print("  O ")
            if turns < 3: print(" /|\\ ")
            if turns < 2: print("  | ")
            if turns < 1: print(" / \\ ")
    print(f"Ты проиграл! Загаданное слово было: {secret}")

while True:
    hangman()
    ans = input("Хочешь сыграть снова? (да или нет): ").strip().lower()
    if ans != 'да':
        print("Спасибо за игру!")
        break
