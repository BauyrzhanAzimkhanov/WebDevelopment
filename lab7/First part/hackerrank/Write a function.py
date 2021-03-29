def is_leap(a):
    print('True' if(a % 4 == 0 and a % 100 != 0 or a % 400 == 0) else 'False')
a = int(input())
is_leap(a)