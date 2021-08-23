# // “екстовый файл 24-6.txt состоит не более чем из 10^6 символов S, T, O, C, K.
# // —колько раз встречаетс€ комбинаци€ ЂOCKї, не €вл€юща€с€ при этом частью
# // комбинации ЂSTOCKї.

with open("input_files/24-6.txt", 'r') as file:
    input_data = file.read()

input_data = input_data.replace("STOCK", "")

print(input_data.count("OCK"))