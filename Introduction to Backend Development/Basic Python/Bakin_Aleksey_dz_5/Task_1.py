# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
def odd_nums(num):
    """Генерирует последовательность нечетных чисел."""
    for i in range(1, num + 1):
        if i % 2 != 0:
            yield i


odd_to_19 = odd_nums(19)
for j in range(19):
    print(next(odd_to_19))