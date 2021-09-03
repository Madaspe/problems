#
# // Рассматривается множество целых чисел, принадлежащих числовому отрезку
# // [862346; 1056242]. Найдите числа, нетривиальные делители которых образуют
# // арифметическую прогрессию с разностью d = 100. В ответе для каждого такого
# // числа (в порядке возрастания) запишите сначала само число, а потом – его
# // максимальный нетривиальный делитель.
from math import sqrt

def get_all_divisors(number):
    divisors = []

    for divisor in range(1, round(sqrt(number) + 1)):
        if number % divisor == 0:
            divisors.append(divisor)
            divisors.append(number // divisor)

    return list(sorted(list(set(divisors))))

# cnt = 0
for num in range(862346, 1056242+1):
    divisors = get_all_divisors(num)[1:-1]

    flag = True
    for index in range(1, len(divisors)):
        if abs(divisors[index-1] - divisors[index]) != 100:
            flag = False
            break

    if flag and len(divisors) >= 2:
        # cnt += 1
        print(num,max(divisors))
# print(cnt)


