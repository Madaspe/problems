# // Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# // отрезку [2358827; 2358891], простые числа. Выведите все найденные простые
# // числа в порядке возрастания, слева от каждого числа выведите его номер по
# // порядку.

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

i = 1
for num in range(2358827, 2358891 + 1):
    if is_prime(num):
        print(i, num)
        i+=1