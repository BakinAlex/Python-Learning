# # 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
#   a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#   Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
#   делится нацело на 7. Внимание: использовать только арифметические операции!
#
division = 0
summa_numbers = 0
odd_numbers_cubed = []
# создаем цикл for для создания списка, состоящего из кубов нечётных чисел от 1 до 1000
for i in range(1, 1001):
    if i % 2 != 0:
        number_cubed = i ** 3
        odd_numbers_cubed.append(number_cubed)
        # создаем цикл for для разделения полученных чисел и проверки их кратности 7
        for num in str(number_cubed):
            division += int(num)
        if division % 7 == 0:
            summa_numbers += number_cubed
        division = 0
print(summa_numbers)


#   b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
#   списка, сумма цифр которых делится нацело на 7.
#   c. * Решить задачу под пунктом b, не создавая новый список.
#
division = 0
summa_numbers = 0
odd_numbers_cubed = []
# создаем цикл for для создания списка, состоящего из кубов нечётных чисел от 1 до 1000
for i in range(1, 1001):
    if i % 2 != 0:
        number_cubed = (i ** 3) + 17
        odd_numbers_cubed.append(number_cubed)
        # создаем цикл for для разделения полученных чисел и проверки их кратности 7
        for num in str(number_cubed):
            division += int(num)
        if division % 7 == 0:
            summa_numbers += number_cubed
        division = 0
print(summa_numbers)
