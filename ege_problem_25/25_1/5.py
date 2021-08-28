# // Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# // отрезку [573213; 575340] число с минимальной  суммой делителей, имеющее
# // ровно четыре делителя. Для найденного числа выведите сумму делителей,
# // количество делителей и все делители в порядке убывания.


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

min_sum = 10**10
current_divisors = 0
for i in range(573213, 575340+1):
    divisors = get_all_divisors(i)

    if len(divisors) == 4 and min_sum > sum(divisors):
        min_sum = sum(divisors)
        current_divisors = divisors.copy()

print(min_sum, len(current_divisors), *sorted(current_divisors, reverse=True))