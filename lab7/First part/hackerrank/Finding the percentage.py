n = int(input())
ans = []
for i in range(n):
    a = input().split()
    ans.append(a)
finding = input()
summ = 0
for i in range(n):
    if(ans[i][0] == finding):
        for j in range(1, len(ans[i])):
            summ = float(summ) + float(ans[i][j])
print(summ / (len(ans[0]) - 1))