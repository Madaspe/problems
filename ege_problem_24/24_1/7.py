# // В текстовом файле 24-7.txt находится цепочка из символов, в которую могут
# // входить заглавные буквы латинского алфавита A ... Z и десятичные цифры.
# // Найдите длину самой длинной подцепочки, состоящей из одинаковых символов.
# // Если в файле несколько подходящих цепочек одинаковой длины, нужно взять
# // первую из них. Для каждой цепочки максимальной длины выведите в отдельной
# // строке сначала символ, из которого строится эта цепочка, а затем через
# // пробел – длину этой цепочки.

already = []


def get_max(string):
    len_max = 0
    char_max = ''
    char_previous = string[0]
    len_current = 0

    for char in string[1:]:
        if char == char_previous:
            len_current += 1
        else:
            len_current = 1

        if len_current > len_max and char not in already:
            char_max = char
            len_max = len_current

        char_previous = char

    return len_max, char_max


def solve(filename):
    global already
    with open(f"input_txt/{filename}", 'r') as file:
        string = file.read()

    for _ in range(20):
        len_max, char = get_max(string)
        already.append(char)
        print(len_max, char)

    return get_max(string)


if __name__ == '__main__':
    # tests()
    print(f"solve for 24-7.txt is {solve('24-7.txt')}")
