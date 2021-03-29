import array as arr
n = int(input())
a = []
a = input().split(" ")
temp = 0
for i in range(n // 2):
    temp = a[i]
    a[i] = a[n-i-1]
    a[n-i-1] = temp    
for i in a:
    print(i, end=" ")