# // ¬ текстовом файле 24-7.txt находитс€ цепочка из символов, в которую могут
# // входить заглавные буквы латинского алфавита A ... Z и дес€тичные цифры.
# // Ќайдите длину самой длинной подцепочки, состо€щей из одинаковых символов.
# // ≈сли в файле несколько подход€щих цепочек одинаковой длины, нужно вз€ть
# // первую из них. ƒл€ каждой цепочки максимальной длины выведите в отдельной
# // строке сначала символ, из которого строитс€ эта цепочка, а затем через
# // пробел Ц длину этой цепочки.

def count(string):
    cnt = 0
    for index in range(0, len(string)):
        slice = string[index: index+5:]

        if len(slice) != 5:
            continue

        check = True
        for slice_index in range(1, len(slice) - 1):
            if slice[slice_index - 1] == slice[slice_index] or slice[slice_index] == slice[slice_index + 1]:
                check = False

        if check:
            cnt += 1
    return cnt

def tests():
    print(count("ABCDEF") == 2,
          count("ABCDEFABCDEF") == 8,
          count("ABCDDEFFAB") == 0,
          count("ABABABABABABAB") == 10,
          count("AAABCABCABCABCABCCC") == 11,
        count("CDAFBBAAADDDEFDEFDEFFFFAAABBCADA") == 7)


def solve(filename):
    with open(f"input_txt/{filename}", 'r') as file:
        string = file.read()

    return count(string)


if __name__ == '__main__':
    tests()
    print(f"solve for 24-5.txt is {solve('24-5.txt')}")