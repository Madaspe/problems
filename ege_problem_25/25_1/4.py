# // Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# // отрезку [194441; 196500] числа (в порядке возрастания) с нечётным
# // количеством делителей. Для каждого такого числа выведите его порядковый
# // номер (начиная с единицы), само число, количество его делителей и делитель,
# // квадрат которого равен этому числу.


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


index = 1
for num in range(194441, 196500 + 1):
    divisors = get_all_divisors(num)

    if len(divisors) % 2 != 0:
        print(index, num,len(divisors), int(sqrt(num)))
        index += 1
