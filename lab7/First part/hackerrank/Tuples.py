n = int(input())
a = input().split()
t = tuple(int(i) for i in a)
print(hash(t))