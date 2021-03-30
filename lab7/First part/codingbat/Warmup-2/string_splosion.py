def string_splosion(string):
    ans = ''
    for i in range(len(string)):
        ans += string[:i+1]
    return ans