# # Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
#   до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
#   * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Введите продолжительность: '))

if duration < 60:
    print(f'{duration} сек')
elif duration < 3600:
    minute = duration // 60
    seconds = duration - (minute * 60)
    print(f'{minute} мин {seconds} сек')
elif duration < 86400:
    hours = duration // 3600
    minute = (duration - (hours * 3600)) // 60
    seconds = duration - (hours * 3600) - (minute * 60)
    print(f'{hours} час {minute} мин {seconds} сек')
else:
    day = duration // 86400
    hours = (duration - (day * 86400)) // 3600
    minute = (duration - (day * 86400) - (hours * 3600)) // 60
    seconds = duration - (day * 86400) - (hours * 3600) - (minute * 60)
    print(f'{day} дн {hours} час {minute} мин {seconds} сек')
