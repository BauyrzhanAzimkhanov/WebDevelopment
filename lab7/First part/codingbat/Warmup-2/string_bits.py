def string_bits(string):
    ans = ''
    for i in range(len(string)):
        if(i % 2 == 0):
            ans += string[i]
    return ans