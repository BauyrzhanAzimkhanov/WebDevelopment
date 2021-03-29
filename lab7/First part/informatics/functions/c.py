def xor(x, y):
    if(((x == 1 or x == True) and (y == 0 or y == False)) or ((x == 0 or x == False) and (y == 1 or y == True))):
        print(1)
    else:
        print(0)
string = input().split()
x = int(string[0])
y = int(string[1])
xor(x, y)