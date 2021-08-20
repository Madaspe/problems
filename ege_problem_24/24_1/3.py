# // ¬ текстовом файле 24-3.txt находитс€ цепочка из символов латинского алфавита
# // A, B, C, D, E, F. Ќайдите максимальную длину цепочки вида DBACDBACDBAC...
# // (составленной из фрагментов DBAC, последний фрагмент может быть неполным).


def count(string):
    chars = ['D', 'B', 'A', 'C']
    sub_str = 'D'
    len_current = 0
    len_max = 0

    while sub_str in string:
        len_current += 1
        len_max = max(len_current, len_max)
        sub_str += chars[(chars.index(sub_str[-1]) + 1) % 4]

    print(sub_str)
    return len_max


def tests():
    print(count("A") == 1,
          count("ABDE") == 4,
          count("ABCDEEF") == 3,
          count("ACBBFDDD") == 3,
          count("EEEEFDDDCBB") == 4,
          count("FABDEECEBDD") == 5,
          count("AABBDDFDDEEAAA") == 7)


def solve(filename):
    with open(f"input_txt/{filename}", 'r') as file:
        string = file.read()

    return count(string)


if __name__ == '__main__':
    tests()
    print(f"solve for 24-3.txt is {solve('24-3.txt')}")