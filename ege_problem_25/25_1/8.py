# // Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# // отрезку [2532000; 2532160], простые числа. Найдите все простые числа, но
# // выведите на экран только каждое третье простое число (то есть числа с
# // порядковыми номерами 1, 4, 7, 10, …). Вывод осуществите в порядке
# // возрастания, слева от каждого числа выведите его собственный порядковый
# // номер среди всех простых чисел.


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
maxx = 0
for num in range(125697, 190234+1):
    divisors = get_all_divisors(num)
    prime_divisors = []
    for i in divisors:
        if is_prime(i):
            prime_divisors.append(i)
    print(len(prime_divisors))
    for i, i1 in enumerate(prime_divisors):
        for j,j1 in enumerate(prime_divisors):
            if i1 != j1 and i1 * j1 == num and i > j:
                maxx += 1
    # maxx = max(cnt, maxx)
print(maxx)