# // Ќапишите программу, котора€ ищет среди целых чисел, принадлежащих числовому
# // отрезку [135743; 135789], числа, имеющие ровно 6 различных делителей.
# // ¬ыведите эти делители дл€ каждого найденного числа в пор€дке возрастани€.

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


for i in range(135743, 135789 + 1):
    if len(get_all_divisors(i)) == 6:
        print(*sorted(get_all_divisors(i)), i)

# 1 3 9 15083 45249 135747 135747
# 1 2 4 33937 67874 135748 135748
# 1 2 4 33941 67882 135764 135764
# 1 5 25 5431 27155 135775 135775