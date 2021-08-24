# // Текстовый файл содержит последовательность из строчных и заглавных букв
# // английского алфавита и цифр. Всего не более 10^6 символов. Назовём локальным
# // минимумом символ, номер которого в кодовой таблице меньше номеров предыдущего
# // и последующего символов. Самый первый и самый последний символ не являются
# // локальными минимумами. Определить наибольшее расстояние между двумя соседними
# // локальными минимумами. Расстоянием между элементами будем считать разность их
# // индексов. Исходные данные записаны в файле 24-4.txt.

with open("input_files/24-4.txt", 'r') as file:
    input_data = [ord(i) for i in file.read()]

local_mins = []

for index in range(1, len(input_data) - 1):
    if input_data[index] < input_data[index - 1] and input_data[index] < input_data[index + 1]:
        local_mins.append(index)

minn = 0
for index in range(1, len(local_mins) - 1):
    minn = max(local_mins[index] - local_mins[index - 1], local_mins[index] - local_mins[index + 1], minn)

print(minn)

