# // ¬ текстовом файле 24-6.txt находитс€ цепочка из символов, в которую могут
# // входить заглавные буквы латинского алфавита A ... Z и дес€тичные цифры.
# // Ќайдите длину самой длинной подцепочки, состо€щей из одинаковых символов.
# // ≈сли в файл несколько цепочек одинаковой длины, нужно вз€ть первую из них.
# // ¬ыведите сначала символ, из которого строитс€ эта подцепочка, а затем через
# // пробел Ц длину этой подцепочки.


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

        if len_current > len_max:
            char_max = char
            len_max = len_current

        char_previous = char

    return len_max, char_max


def solve(filename):
    with open(f"input_txt/{filename}", 'r') as file:
        string = file.read()

    return get_max(string)


if __name__ == '__main__':
    # tests()
    print(f"solve for 24-6.txt is {solve('24-6.txt')}")