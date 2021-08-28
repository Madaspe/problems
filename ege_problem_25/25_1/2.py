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


def get_even_divisors(lst):
    even_divisors = []
    for number in lst:
        if number % 2 == 0:
            even_divisors.append(number)
    return list(set(even_divisors))


for i in range(190201, 190280 + 1):
    divisors = get_all_divisors(i)

    if len(get_even_divisors(divisors)) == 4:
        print(*sorted(get_even_divisors(divisors), reverse=True))

