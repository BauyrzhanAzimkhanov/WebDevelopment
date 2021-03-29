a = int(input())
if(a % 2 == 1 or (a >= 6 and a <= 20)):
    print('Weird')
elif((a >= 2 and a <= 5) or a > 20):
    print('Not Weird')