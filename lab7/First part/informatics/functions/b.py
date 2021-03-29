def power(a, b):
    ans = 1
    if(b == 0):
        print(1)
    else:
        for i in range(1, b + 1):
            ans = ans * a
        print(ans)

string = input().split()
a = float(string[0])
b = int(string[1])
power(a, b)