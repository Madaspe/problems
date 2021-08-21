# // ¬ текстовом файле 24-4.txt находитс€ цепочка из символов латинского алфавита
# // A, B, C, D, E, F. Ќайдите количество цепочек длины 3, удовлетвор€ющих
# // следующим услови€м:
# // a) 2-й символ Ц один из B, D, E;
# // b) 3-й символ Ц один из A, C, D, который не совпадает со вторым;
# // c) 1-й символ Ц совпадает с третьим.



def count(string):
    result = 0
    for char_index in range(2, len(string)):
        if string[char_index] != string[char_index - 1] \
            and string[char_index] in ['A', 'C', 'D'] \
            and string[char_index - 1] != string[char_index] \
            and string[char_index - 1] in ['B', 'D', 'E'] \
            and string[char_index - 2] == string[char_index]:
            result += 1
    return result

def tests():
    print(count("ABA") == 1,
          count("ADAEA") == 2,
          count("DBDEDBDB") == 3,
          count("ABCDEFFEDCBA") == 0,
          count("EABAADAAEACBCCDCCECDBDDDDDEDE") == 8,
            )


def solve(filename):
    with open(f"input_txt/{filename}", 'r') as file:
        string = file.read()

    return count(string)


if __name__ == '__main__':
    tests()
    print(f"solve for 24-4.txt is {solve('24-4.txt')}")