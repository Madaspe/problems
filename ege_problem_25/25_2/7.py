# // Рассматриваются целые числа, принадлежащих числовому отрезку
# // [278932; 325396], которые представляют собой произведение трёх различных
# // простых делителей, оканчивающихся на одну и ту же цифру. В ответе запишите
# // количество таких чисел и максимальное из них.
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
cnt = 0
num_save = 0
for num in range(278932, 325396+1):
    prime_divisors = list(filter(is_prime, get_all_divisors(num)))

    for i, i1 in enumerate(prime_divisors):
        for j, j1 in enumerate(prime_divisors):
            for q, q1 in enumerate(prime_divisors):
                if i>=j>=q and i1*j1*q1 == num and i1 % 10 == j1 % 10 == q1 % 10:
                    cnt += 1
                    num_save = num

print(cnt, num_save)