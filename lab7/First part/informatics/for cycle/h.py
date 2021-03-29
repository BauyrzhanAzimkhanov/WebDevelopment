a = int(input())
ans = a
for i in range(1, a + 1):
    if(a % i == 0):
        print(i, end=" ")