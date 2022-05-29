# # 5. Создать список, содержащий цены на товары (10–20 товаров), например:
#   [57.8, 46.51, 97, ...]
#   Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
#   (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если,
#   например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

from math import trunc
price_list = [85, 130, 112.63, 50.8, 231, 170.33, 15.9, 14.6, 55, 115.5, 86.38, 13.6, 13,
              52, 33.14, 8.1, 196.05]


def prices_list(lst):
    output_price_list = ''
    for i in lst:
        if type(i) == int:
            price_int = str(i)
            output_price_list += f'{price_int} руб 00 коп, '
        else:
            whole_part = trunc(i)
            fractional_part = str(i)[(str(i)).find('.') + 1:]
            if len(fractional_part) == 1:
                fractional_part = fractional_part + '0'
            output_price_list += f'{whole_part} руб {fractional_part} коп, '
    print(output_price_list)


prices_list(price_list)
# print(id(price_list))

#   Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать,
#   что объект списка после сортировки остался тот же).
price_list.sort()
prices_list(price_list)
print(id(price_list))

#   Создать новый список, содержащий те же цены, но отсортированные по убыванию.
revers_price_list = sorted(price_list, reverse=True)
prices_list(revers_price_list)

#   Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
prices_list(price_list[-5:])
