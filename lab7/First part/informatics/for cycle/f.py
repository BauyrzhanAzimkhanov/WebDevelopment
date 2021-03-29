a = int(input())

i = a
ans = ''
cnt = 0
while(i > 0):
    ans = ans + str(i % 10)
    i //= 10
print(int(ans))