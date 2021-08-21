# // Текстовый файл 24-8.txt состоит не более чем из 1000 символов. Определите
# // максимальное количество идущих подряд символов, среди которых каждые два
# // соседних различны.

with open('input_txt/24-8.txt', 'r') as file:
    input_string = file.read()

len_max = 0
len_cur = 0
char_pre = input_string[0]
for char in input_string[1:]:
    if char != char_pre:
        len_cur += 1
    else:
        len_cur = 1

    char_pre = char
    len_max = max(len_cur, len_max)

print(len_max)