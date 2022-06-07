# # 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
#   реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть
#   с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(num):
    dictionary_words = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                        'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

    if num.lower() not in dictionary_words:
        print('None')
    else:
        if num[0].isupper() is True:
            print(dictionary_words[num.lower()].capitalize())
        else:
            print(dictionary_words[num])


num_translate_adv('Eight')
