# Дано четырехзначное число. Проверить, является ли оно «счастливым билетом».  task 1

ticket_number=list(input('Enter ticket number '))
l_s = int(len(ticket_number))

if l%2==0:
    i=0
    sum1=0
    sum2=0
    while i<(l_s/2):
        sum1=sum1+int(ticket_number[i])
        sum2=sum2+int(ticket_number[i+int(l_s/2)])
        i=i+1
    if sum1==sum2: print('Happy ticket!')
    else:
        print('Oops!')
else:
    print('Wrong ticket number')

# С клавиатуры вводится шестизначное число. Проверить, является ли оно палиндромом      task2

number=list(input('Enter a number '))
number1=number.copy()
number.reverse()

if number==number1:
    print('Number is the palindrom')
else:
    print('Number is not the palindrom')


# Есть круг с центром в начале координат и радиусом 4.          task 3
# Пользователь вводит с клавиатуры координаты точки x и y.
# Написать программу, которая определит, лежит ли эта точка внутри круга или нет.

x= float(input("x = "))
y = float(input("y = "))
radius = float(input("Radius = "))

if (x ** 2 + y ** 2)**0.5 <= radius:
    print('Point is in the circle')
else:
    print('Point is not in the circle')