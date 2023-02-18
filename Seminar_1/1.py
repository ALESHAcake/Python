# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))

one_figure = number % 10
two_figure = number % 100 // 10
three_figure = number // 100

sum = one_figure + two_figure + three_figure

print(f'Сумма цифр трехзначного числа: {sum}')

