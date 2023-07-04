all_num = int(input('Введите три числа '))

num3 = all_num % 10
num1 = all_num // 100 

if all_num > 999 :
    print('Слишком большое число')
else:
    print(num1,num3, sep='')


