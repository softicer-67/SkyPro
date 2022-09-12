from time import time


with open('russian_word.txt', 'r', encoding='utf-8') as f:
    file = [i.rstrip('\n') for i in f]


def timeit(func):
    def wrapper(word, word_list):
        start = time()
        print('=' * 50)
        result = func(word, word_list)
        print(time() - start)
        return result
    return wrapper


@timeit
def check_word_my(word, word_list):
    for i in word_list:
        if i == word:
            return 'Found!', word
    return 'NotFound'


print(check_word_my('ясень', file))
print(check_word_my('кот', file))


@timeit
def check_word(word, word_list):
    if word in word_list[:len(word_list)//2]:
        return 'Found!', word
    else:
        if len(word_list) != 1:
            if word in word_list:
                return 'Found!', word
            return False
        check_word(word, word_list[len(word_list)//2:])
    return False


print(check_word('ясень', file))
print(check_word('кот', file))


