# Выведите на экран все числа в диапазоне от 1 до 100 кратные 7 task1

begin_number=int(input('begin_number = '))
last_number=int(input('last_number = '))
i=begin_number
while i<last_number:
    if not i%7:
        print(i)
    i+=1

# Вычислить с помощью цикла факториал числа n введенного с клавиатуры (4<n<16).
# Факториал числа - это произведение всех чисел от этого числа до 1. Например, 5!=5*4*3*2*1=120     task2

number=int(input('number = '))
left_limit=int(input('left_limit= '))
right_limit=int(input('right_limit= '))
fct = 1
if left_limit < number < right_limit:
    i=1

    while i<=number:
        fct = fct * i
        i+=1

print('factorial = ', fct)

# Напечатайте таблицу умножения на 5. Предпочтительно печатать 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10 и т. д. task3

num1=int(input('num1 = '))
LIMIT=10
i=1

while i <= LIMIT :
    print(i, ' x ',num1, ' = ', i*num1)
    i+=1

# Выведите на экран прямоугольник из *. Причем, высота и ширина прямоугольника вводятся с клавиатуры.   task4

height = int(input('height  > 2 '))
width = int(input('width  > 3 '))
i=1

while  i <= height :
    if i == 1 or i == height :
        print('*' * width)
    else :
        print('*',' ' * (width - 4), '*')
    i+=1

# Дан список [0,5,2,4,7,1,3,19]. Написать программу для подсчета нечетных цифр в нем.   task 5
list_1 =list(input('Enter the number '))
print(list_1)
s1=0

for x in list_1:
    if int(x)%2:
        s1= s1 + 1

print (s1)

# Создайте список случайных чисел (размером 4 элемента).
# Создайте второй список в два раза больше первого,
# где первые 4 элемента должны быть равны элементам первого списка,
# а остальные элементы заполните удвоенными значением начальных.
# Например, Было →  [1,4,7,2] Стало → [1,4,7,2,2,8,14,4]        task 6

import random
Q_TY=4
list_2=[]

for i in range(Q_TY):
    list_2.append(random.randint(1,Q_TY))

list_3=list_2.copy()

for x in list_2:
    list_3.append(int(x*2))

print(list_2)
print(list_3)

# Создайте список из 12 элементов.
# Каждый элемент этого списка представляет собой  зарплату рабочего за месяц
# (случайное число от 7500 до 15000 грн.). Выведите этот список на экран
# и вычислите среднемесячную зарплату этого рабочего.                           task 7

num_of_workers = int(input('Number of workers '))
min_salary = int(input('Min salary '))
max_salary = int(input('Max salary '))
salary=[]
m_salary=0

for i in range(num_of_workers):
    salary.append(random.randint(min_salary,max_salary))
    m_salary=m_salary + salary[i]

print ('Salary of workers ', salary)
print ('Middle salary is ',m_salary/num_of_workers, 'uah' )

# )Представьте в виде списка списков матрицу
# [  1,  2 ,   3,   4]
# [  5,  6 ,   7,   8]
# [  9,10, 11, 12]
# [13,14, 15, 16]                                                               task8
# Напишите программу, которая выведет эту матрицу на экран, вычислит и выведет сумму элементов этой матрицы.

ROW_COL=4
i=0

matr=[]
s2=0

while i<=ROW_COL-1:
    j = 0
    matr1=[]
    while j<=ROW_COL-1:
        x = int(input('number '))
        matr1.append(x)
        s2=s2+ x
        j+=1
    matr.append(matr1)
    i+=1

for i in matr :
    print (i)

print ('sum = ', s2)

