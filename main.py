import random
import shutil
from letters import letter
import os


WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'
BLUE = '\033[1;36m'

letters = letter

all_letters = ''
for k, v in letters.items():
    all_letters += k * v

# Считываю все буквы из файла, добавляю из по запросу к функции в игру и удаляю эти буквы из файла.
# Делаю проверку, если букв осталось меньше чем нужно дабавить в игре - Выход
def get_letters(num):    
    global all_letters
    rnd = ''
    if len(all_letters) < num:
        exit('Закончились буквы. Game Over.')
    for i in range(num):
        x = random.choice(range(len(all_letters)))
        rnd += all_letters[x]
        all_letters = all_letters[:x] + all_letters[x + 1:]
    return rnd


# Логика игры
def main():    
    if os.path.exists('tmp/'):
        pass
    else:
        os.mkdir('tmp/')

    print('Привет.\nМы начинаем играть в Scrabble')
    first_player = input('Как зовут первого игрока? ')
    print(first_player)
    second_player = input('Как зовут второго игрока? ')
    print(second_player)

    print(f'{first_player} vs {second_player}\n(раздаю случайные буквы)')

    letters_one = get_letters(7)
    letters_two = get_letters(7)

    print(f'{GREEN}{first_player.upper()}{WHITE} - буквы: {letters_one}')
    print(f'{GREEN}{second_player.upper()}{WHITE} - буквы: {letters_two}')

    with open(f'tmp/game_{first_player}.txt', 'w', encoding='utf-8') as f:
        f.write(letters_one)

    with open(f'tmp/game_{second_player}.txt', 'w', encoding='utf-8') as f:
        f.write(letters_two)

    game = 1
    score_user_1 = 0
    score_user_2 = 0

    while True:

        if game % 2 != 0:
            user = first_player.upper()
            let = letters_one
        else:
            user = second_player.upper()
            let = letters_two

        print(f'\nХодит {GREEN}{user}{WHITE}')

        with open(f'tmp/game_{user}.txt', 'r', encoding='utf-8') as f:
            text = f.read()
            print(f'Составь слово из букв: {BLUE}{" ".join(text.upper())}{WHITE}')

        word = input().lower()

        if word == 'stop':
            print(f'{GREEN}Игрок {RED}{user}{GREEN} решил остановить игру.\n\t\t{RED}До свидания!{WHITE}')
            print(f'\t{RED} Результат: {GREEN}{score_user_1}{RED} vs {GREEN}{score_user_2}{WHITE}')
            file_path = 'tmp'
            shutil.rmtree(file_path)
            break

        if word == '':
            print('Пустой ввод, попробуй еще раз ')
            continue
        elif any(map(str.isdigit, word)):
            print("В слове есть цифры. Попробуйте еще.")
            continue

        for i in word.upper():
            if i not in let:
                print("Делайте выбор только из ваших букв")
                break

        else:
            with open('russian_word.txt', 'r', encoding='utf-8') as fl:
                file = fl.read()

            bonus = 0

            if word in file and len(word) >= 3:
                len_word = len(word)
                if len_word == 3:
                    bonus = 3
                elif len_word > 3:
                    bonus = len_word + 2

                add_letter = get_letters(len_word + 1)
                print(f'Такое слово есть.\n{user} получает {bonus} баллов\nДобавляю буквы: {add_letter}')

                if game % 2 == 0:
                    score_user_2 += 1
                else:
                    score_user_1 += 1

                with open(f'tmp/game_{user}.txt', 'r', encoding='utf-8') as fl:
                    fe = fl.read()

                add = ''
                for i in fe.lower():
                    if i in word or i in add:
                        add += ''
                    else:
                        add += i

                    with open(f'tmp/game_{user}.txt', 'w', encoding='utf-8') as fil:
                        fil.write(add)

                    with open(f'tmp/game_{user}.txt', 'a', encoding='utf-8') as fil:
                        fil.write(add_letter)

            else:
                add_letter = get_letters(1)
                print(f'Такого слова нет.\n{user} не получает очков.\nДобавляю 1 букву: {add_letter}')

        print(f'{RED}Результат: {GREEN}{score_user_1}{RED} vs {GREEN}{score_user_2}{WHITE}')
        game += 1


if __name__ == '__main__':
    main()
