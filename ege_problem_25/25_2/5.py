# // Среди целых чисел, принадлежащих числовому отрезку [351627;428763],
# // найдите числа, которые представляют собой произведение двух различных
# // простых делителей. Запишите в ответе количество таких чисел и их среднее
# // арифметическое. Для среднего арифметического запишите только целую часть
# // числа.

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

sum_divs = 0
count_divs = 0
for num in range(351627,428763+1):
    divisors = get_all_divisors(num)
    prime_divisors = list(filter(is_prime, divisors))
    break_flag = False
    for i, i1 in enumerate(prime_divisors):
        for j, j1 in enumerate(prime_divisors):
            if i != j and i1 * j1 == num:
                count_divs += 1
                sum_divs += num

                break_flag = True
                break
        if break_flag:
            break

print(count_divs,sum_divs/count_divs)