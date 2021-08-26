def check(num):
    s = str(num)

    for index, char in enumerate(s):
        digit = int(char)
        if (index == 2 or index == 4) and (digit % 2 == 0):
            continue
        elif digit % 2 != 0 and index != 2 and index != 4:
            continue
        else:
            return False

    return True

all_number = []
for i in range(1, 1000000):
    if not check(i):
        continue
    if i % 6 != 0 and i % 7 != 0 and i % 8 != 0:
        all_number.append(i)
print(len(all_number), max(all_number) - min(all_number))

