import array as arr
n = int(input())
a = []
a = input().split(" ")
ans = 0
for i in range(n):
    if(int(a[i]) > 0):
        ans += 1
print(ans)