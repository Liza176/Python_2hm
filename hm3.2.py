all_num = int(input('Введите три числа '))

num3 = all_num % 10
num1 = all_num // 100
all_num = all_num // 10 % 10

if all_num > 999 :
    print('Слишком большое число')
else:
    print(num3,all_num,num1, sep='')


