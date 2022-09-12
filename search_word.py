from time import time


with open('russian_word.txt', 'r', encoding='utf-8') as f:
    file = [i.rstrip('\n') for i in f]


def timeit(func):
    def wrapper(a, b):
        start = time()
        print('=' * 50)
        result = func(a, b)
        print(time() - start)
        return result
    return wrapper


@timeit
def check_word_my(word, word_list):
    for i in word_list:
        if i == word:
            return 'Found!', i
    return 'NotFound'


print(check_word_my('ясень', file))
print(check_word_my('кот', file))

'''
=========================
0.0576167106628418
('Found!', 'ясень')
=========================
0.01562356948852539
('Found!', 'кот')
=========================
'''

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

'''
=========================
0.10252952575683594
('Found!', 'ясень')
=========================
0.04003643989562988
('Found!', 'кот')
=========================
'''

