# // Рассматриваются целые числа, принадлежащих числовому отрезку
# // [523456; 578925], которые представляют собой произведение двух различных
# // простых делителей. Найдите такое из этих чисел, у которого два простых
# // делителя меньше всего отличаются друг от друга. В ответе запишите простые
# // делители этого числа в порядке возрастания. Если подходящих чисел несколько,
# // запишите в ответе делители наименьшего из них.
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


min_sum = 100 ** 10
num_save = 0
prime_divisors_save = []
for num in range(523456, 578925 + 1):
    divisors = get_all_divisors(num)
    prime_divisors = list(filter(is_prime, divisors))

    for i, i1 in enumerate(prime_divisors):
        for j, j1 in enumerate(prime_divisors):
            if i < j and i != j and i1 * j1 == num and abs(i1 - j1) < min_sum and num_save < num:
                min_sum = abs(i1 - j1)
                num_save = num
                prime_divisors_save = prime_divisors.copy()

print(*sorted(prime_divisors_save))
