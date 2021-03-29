a = int(input())
b = int(input())
#if((a//1000 >= 1 and a//1000 <= 9 and a//1000 == a%10 and (a//100)%10 == (a//10)%10 and b == 1) or ((a//1000 > 9 or a//1000 == 0 or a//1000 != a%10 or a//100 != (a//10)%10) and b != 1)):
#    print()
print('YES' if((a//1000 >= 1 and a//1000 <= 9 and a//1000 == a%10 and (a//100)%10 == (a//10)%10 and b == 1) or ((a//1000 > 9 or a//1000 == 0 or a//1000 != a%10 or a//100 != (a//10)%10) and b != 1)) else 'NO')