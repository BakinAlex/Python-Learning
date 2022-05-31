# # 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
#   «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
#   по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
#   >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
#   Как поступить, если потребуется сортировка по ключам?

def thesaurus_adv(*args):
    dictionary_name = {}
    for i in args:
        lst_name = i.split(' ')
        dictionary_name[lst_name[1][0]] = dictionary_name.get(lst_name[1][0], {})
        dictionary_name[lst_name[1][0]][lst_name[0][0]] = dictionary_name[lst_name[1][0]].get(lst_name[0][0], []) + [i]
    print(dictionary_name)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")