# // Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# // отрезку [2532000; 2532160], простые числа. Найдите все простые числа, но
# // выведите на экран только каждое третье простое число (то есть числа с
# // порядковыми номерами 1, 4, 7, 10, …). Вывод осуществите в порядке
# // возрастания, слева от каждого числа выведите его собственный порядковый
# // номер среди всех простых чисел.


from math import sqrt


def get_all_divisors(number):
    divisors = []

    for divisor in range(1, round(sqrt(number) + 1)):
        if number % divisor == 0:
            divisors.append(divisor)
            divisors.append(number // divisor)

    return list(set(divisors))


def is_prime(number):
    return True if len(get_all_divisors(number)) == 2 else False

i=1
print()
for num in range(2532000, 2532160+1):
    if is_prime(num):
        if i in list(range(1, 100, 3)):
            print(i, num)
        i += 1