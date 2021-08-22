# // Текстовый файл 24-5.txt содержит последовательность из символов «(»и «)»,
# // всего не более 10^6 символов. Определить, с какого по счёту символа от начала
# // файла начинается 10000-я пара скобок «()».


with open("input_files/24-5.txt", 'r') as file:
    input_data = file.read()

count = 0
for index in range(1, len(input_data)):
    if input_data[index] == ')' and input_data[index - 1] == '(':
        count += 1
    if count == 10000:
        print(index)
