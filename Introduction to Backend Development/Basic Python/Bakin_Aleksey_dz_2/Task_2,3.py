# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.
#
# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до
# двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

init_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
ex_list = []

for i in init_lst:
    number_index = init_lst.index(str(i))
    if i.isdigit() == True:
        if i not in ex_list:
            init_lst.insert(number_index, '"')
            ex_list.append(i)
            continue
    if i.isdigit() == True:
        init_lst.insert(number_index + 1, '"')
        if len(i) < 2:
            change_word = '0' + i
            init_lst[number_index] = change_word
    if '+' in i:
        if i not in ex_list:
            init_lst.insert(number_index, '"')
            ex_list.append(i)
            continue
        degrees = '0'.join(i)
        degrees_index = init_lst.index(i)
        init_lst[degrees_index] = degrees
        init_lst.insert(degrees_index + 1, '"')

print(' '.join(init_lst))
