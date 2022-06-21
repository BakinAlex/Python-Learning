import requests
import datetime as dt


def currency_rates(money):
    """Запрашиваем на сайте курс валют
           Принимаем валюту в формате RUB,EUR """
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get ( URL )
    answer_json = response.json ( )
    if dict ( answer_json[ 'Valute' ] ).get ( f'{money.upper ( )}' , None ) is None :
        return None
    else :
        date_time_str = answer_json[ 'Date' ]
        date_time_obj = dt.datetime.strptime ( date_time_str , '%Y-%m-%dT%H:%M:%S%z' )
        answer = f"Время: {date_time_obj.strftime ( '%Y-%m-%d %H:%M:%S' )}\n" \
                 f"Валюта: {(answer_json[ 'Valute' ][ f'{money.upper ( )}' ][ 'Name' ])}\n" \
                 f"Стоимость: {answer_json[ 'Valute' ][ f'{money.upper ( )}' ][ 'Value' ]} руб\n"
        return answer