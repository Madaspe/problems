# // ¬ текстовом файле 24-1.txt находитс€ цепочка из символов латинского алфавита
# // X, Y, Z. Ќайдите длину самой длинной подцепочки, состо€щей из символов Z.

def count(string):
    sub_string = "Z"
    len_max = 0
    current_len = 0
    while sub_string in string:
        sub_string += 'Z'
        current_len += 1

        len_max = max(current_len, len_max)

    return len_max

def solve(filename):
    with open(f"input_txt/{filename}", 'r') as file:
        string = file.read()

    return count(string)


def tests():
    print(count("XYZ") == 1)
    print(count("X") == 0)
    print(count("XZZZXZZZZ") == 4)

    print(f"solve for 24-1.txt is {solve('24-1.txt')}")

if __name__ == '__main__':
    tests()