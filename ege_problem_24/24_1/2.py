# // ¬ текстовом файле 24-2.txt находитс€ цепочка из символов латинского алфавита
# // A, B, C, D, E, F. Ќайдите длину самой длинной подцепочки, не содержащей
# // символов C и F.

def count(string):
    len_current = 0
    len_max = 0
    for char in string:
        if char in ['C', 'F']:
            len_current = 0
            continue
        len_current += 1
        len_max = max(len_current, len_max)
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
    print(f"solve for 24-2.txt is {solve('24-2.txt')}")
