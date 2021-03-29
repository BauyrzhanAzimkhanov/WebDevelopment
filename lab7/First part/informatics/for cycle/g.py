a = int(input())
ans = a
for i in range(a, 1, -1):
    if(a % i == 0 and (a % i) < ans):
        ans = i
print(ans)