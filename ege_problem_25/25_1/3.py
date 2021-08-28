# // Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# // отрезку [286564; 287270], числа, имеющие максимальное количество различных
# // делителей. Если таких чисел несколько, то найдите максимальное из них.
# // Выведите количество делителей найденного числа и два наибольших делителя в
# // порядке убывания.

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


maxx = get_all_divisors(286564)
number = 286564
for i in range(286564+1, 287270+1):
    divisors = get_all_divisors(i)

    if len(maxx) < len(divisors) or (len(maxx) == len(divisors) and number < i):
        number = i
        maxx = divisors

print(len(maxx), *reversed(sorted(maxx, reverse=True)[:2]))