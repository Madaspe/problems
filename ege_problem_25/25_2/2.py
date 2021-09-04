# // Среди целых  чисел, принадлежащих числовому отрезку [4099; 26985],
# // найдите числа, имеющие ровно один натуральный делитель, не считая единицы
# // и самого числа. Ответом будет сумма цифр найденных чисел.

from math import sqrt


def get_divisors(number):
    divisors = []

    for divisor in range(1, round(sqrt(number) + 1)):
        if number % divisor == 0:
            divisors.append(divisor)
            divisors.append(number // divisor)

    return sorted(list(set(divisors)))

def get_sum(number):
    ans = 0
    for i in str(number):
        ans += int(i)

    return ans

answer = 0
for i in range(4099, 26985+1):
    divisors = get_divisors(i)
    if len(divisors) == 3:
        answer += get_sum(i)
print(answer)