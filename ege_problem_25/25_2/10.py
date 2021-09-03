#
# // Для интервала [33333;55555] найдите числа, которые кратны сумме своих простых
# // собственных делителей (меньших самого числа). В качестве ответа приведите в
# // порядке возрастания числа, для которых сумма простых делителей больше 250,
# // после каждого числа запишите сумму его простых собственных делителей.
from math import sqrt


def get_all_divisors(number):
    divisors = []

    for divisor in range(1, round(sqrt(number) + 1)):
        if number % divisor == 0:
            divisors.append(divisor)
            divisors.append(number // divisor)

    return list(sorted(list(set(divisors))))


def is_prime(number):
    return True if len(get_all_divisors(number)) == 2 else False


for num in range(33333, 55555 + 1):
    prime_divisors_sum = sum(list(filter(is_prime, get_all_divisors(num)[:-1])))

    if prime_divisors_sum > 250 and num % prime_divisors_sum == 0:
        print(num, prime_divisors_sum)

