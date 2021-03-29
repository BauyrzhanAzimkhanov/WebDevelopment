a = input()
b = input().split()

a = a[0 : int(b[0]) - 1] + str(b[1]) + a[int(b[0]):]
print(a)