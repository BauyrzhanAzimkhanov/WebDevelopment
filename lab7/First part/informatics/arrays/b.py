import array as arr
n = int(input())
a = []
a = input().split(" ")
for i in range(n):
    if(int(a[i]) % 2 == 0):
        print(a[i], end=" ")