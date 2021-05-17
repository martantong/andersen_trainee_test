array = input('Введите числа через пробел: ').split()
for number in array:
    if not int(number) % 3:
        print(number)
