#
# // Среди целых чисел, принадлежащих числовому отрезку [333555; 777999],
# // найдите числа, среди делителей которых есть ровно 35 двузначных чисел.
# // Для каждого найденного числа запишите в ответе само число, наименьший и
# // наибольший из его двузначных делителей. Так, например, для числа 36
# // учитываются только делители 12 и 18.
from math import sqrt


def get_divisors(number):
    divisors = []

    for divisor in range(1, round(sqrt(number) + 1)):
        if number % divisor == 0:
            divisors.append(divisor)
            divisors.append(number // divisor)

    return sorted(list(set(divisors)))


for i in range(333555, 777999 + 1):
    divisors = get_divisors(i)
    count_divisors = 0
    for divisor in divisors:
        if 10 <= divisor <= 99:
            count_divisors += 1
    if count_divisors == 35:
        print(i, min(filter(lambda x: len(str(x)) == 2, divisors)), max(filter(lambda x: len(str(x)) == 2, divisors)))
