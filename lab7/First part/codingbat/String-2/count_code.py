def count_code(string):
    return sum(1 for i in range(len(string) - 3) if string[i:i + 2] == 'co' and string[i + 3] == 'e')