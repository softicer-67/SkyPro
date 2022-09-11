import random
from letters import letter


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
def random_letter(num):
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

    print('Привет.\nМы начинаем играть в Scrabble')
    first_player = input('Как зовут первого игрока? ')
    print(first_player)
    second_player = input('Как зовут второго игрока? ')
    print(second_player)

    print(f'{first_player} vs {second_player}\n(раздаю случайные буквы)')

    letters_one = random_letter(7)
    letters_two = random_letter(7)

    print(f'{GREEN}{first_player.upper()}{WHITE} - буквы: {letters_one}')
    print(f'{GREEN}{second_player.upper()}{WHITE} - буквы: {letters_two}')

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
        print(f'Составь слово из букв: {BLUE}{" ".join(let.upper())}{WHITE}')
        word = input().lower()

        if word == 'stop':
            print(f'{GREEN}Игрок {RED}{user}{GREEN} решил остановить игру.\n\t\t{RED}До свидания!{WHITE}')
            print(f'\t{RED} Результат: {GREEN}{score_user_1}{RED} vs {GREEN}{score_user_2}{WHITE}')
            break

        elif word == '':
            print('Пустой ввод, попробуй еще раз ')
            continue

        elif any(map(str.isdigit, word)):
            print("В слове есть цифры. Попробуйте еще.")
            continue

        elif [i for i in word.upper() if i not in let]:
            print("Делайте выбор только из ваших букв")
            continue
        elif [i for i in word.upper() if i in let]:
            with open('russian_word.txt', 'r', encoding='utf-8') as f:
                file = f.read()

            bonus = 0
            if word in file and len(word) >= 3:
                len_word = len(word)
                if len_word == 3:
                    bonus = 3
                elif len_word > 3:
                    bonus = len_word + 2

                add_letter = random_letter(len_word + 1)
                print(f'Такое слово есть.\n{user} получает {bonus} баллов\nДобавляю буквы: {add_letter}')

                                if game % 2 == 0:
                    score_user_2 += 1
                    
                    add = ''
                    for i in letters_two.lower():
                        if i in word:
                            del i
                        else:
                            add += i
                    letters_two = add + add_letter

                else:
                    score_user_1 += 1

                    add = ''
                    for i in letters_one.lower():
                        if i in word:
                            del i
                        else:
                            add += i
                    letters_one = add + add_letter
            else:

                add_letter = random_letter(1)
                print(f'Такого слова нет.\n{user} не получает очков.\nДобавляю 1 букву: {add_letter}')

        print(f'{RED}Результат: {GREEN}{score_user_1}{RED} vs {GREEN}{score_user_2}{WHITE}')
        game += 1


if __name__ == '__main__':
    main()
