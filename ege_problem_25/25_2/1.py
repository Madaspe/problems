# // Число называется полусовершенным, если сумма всех или некоторых его
# // собственных делителей (то есть всех положительных делителей, отличных от
# // самого́ числа) совпадает с самим этим числом. Определите количество
# // полусовершенных чисел в диапазоне [2; 2000].
from math import sqrt


def get_divisors(number):
    divisors = []

    for divisor in range(1, round(sqrt(number) + 1)):
        if number % divisor == 0:
            divisors.append(divisor)
            divisors.append(number // divisor)

    return sorted(list(set(divisors)))

ans = 0

for num in range(2, 2000 + 1):
    divisors = list(reversed(get_divisors(num)))[1:]
    break_flag = False
    for i in range(len(divisors)*2):
        temp = num
        for divisor in divisors[i:]:
            if temp - divisor > 0:
                temp -= divisor
            elif temp - divisor == 0:
                ans += 1

                break_flag = True
                break
        if break_flag:
            break

print(ans)