# // Текстовый файл 24-1.txt состоит не более чем из 10^6 символов.
# // Определите минимальное чётное число, записанное в этом файле.
# // ЗАМЕЧАНИЕ: под числом подразумевается последовательность цифр,
# // ограниченная другими символами (не цифрами).


with open("input_files/24-1.txt", 'r') as file:
    input_data = file.read()

max_int = 100000000000000000
int_str = ""

for char in input_data:
    if char.isdigit():
        int_str += char
    else:
        try:
            max_int = min(max_int, int(int_str)) if int(int_str) % 2 == 0 else max_int
        except ValueError:
            pass
        int_str = ''

print(max_int)