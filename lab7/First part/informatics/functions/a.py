def min(a, b, c, d):
    if(a < b):
        if(c < d):
            if(a < c):
                print(a)
            else:
                print(c)
        else:
            if(a < d):
                print(a)
            else:
                print(d)
    else:
        if(c < d):
            if(b < c):
                print(b)
            else:
                print(c)
        else:
            if(d < b):
                print(d)
            else:
                print(b)
string = input().split(" ")
a = int(string[0])
b = int(string[1])
c = int(string[2])
d = int(string[3])
min(a, b, c, d)