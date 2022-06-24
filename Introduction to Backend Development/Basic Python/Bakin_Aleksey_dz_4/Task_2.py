# # 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
#   и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
#   использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
#   браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
#   Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
#   величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
#   аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от
#   того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.


import requests
import datetime as dt

def currency_rates(money):
    """Запрашиваем на сайте курс валют
       Принимаем валюту в формате RUB,EUR """
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get ( URL )
    answer_json=response.json()
    date_time_str = answer_json['Date']
    date_time_obj = dt.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S%z')
    answer = f"Время: {date_time_obj.strftime('%Y-%m-%d %H:%M:%S')}\nВалюта: {(answer_json['Valute'][f'{money}']['Name'] )}\n" \
             f"Стоимость: {answer_json['Valute'][f'{money}']['Value']} руб\n"
    return answer

print(currency_rates("USD"))
print(currency_rates("EUR"))


