# // Текстовый файл 24-2.txt состоит не более чем из 10^6 символов.
# // Определите самое большое число, состоящее только из нечётных цифр.
# // ЗАМЕЧАНИЕ: под числом подразумевается последовательность цифр,
# // ограниченная другими символами (не цифрами).

def check_int(number):
    for num in number[1:]:
        if int(num) % 2 == 0:
            return False
    return True

with open("input_files/24-2.txt", 'r') as file:
    input_data = file.read()

max_int = 0
int_str = "0"

for char in input_data:
    if char.isdigit():
        int_str += char
    elif check_int(int_str):
        max_int = max(max_int, int(int_str))
        int_str = '0'
    else:
        int_str = '0'

print(max_int)