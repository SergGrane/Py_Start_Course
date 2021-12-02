# Напишите программу, которая посчитает сколько букв «b» в введенной строке текста. task1

Str1 ='abbbbaaaaabbr'
Symb='b'
print(Str1.count(Symb))

# Считайте строку, которая будет представлять имя человека, введенное с клавиатуры.  task 2
# в имени человека не может быть цифр, оно должно начинаться с большой буквы, за которой должны следовать маленькие.

name=input('Name ')
if name[0].isupper():
    for i in range(1,len(name)):
        if name[i].isdigit() or name[i].isupper():
            print('Error')
            break
else:
    print('Error')

# Напишите программу, которая вычислит сумму всех кодов символов строки.    task 3
Str2= 'Qwerwrt34511'
s=0

for i in (Str2):
    s=s+ord(i)

print('Summa = ',s)

# Выведите на экран 10 строк со значением числа Pi. В первой строке должно быть 2 знака после запятой,
# во второй 3 и так далее.                                                    task 4

import math
Last=10
j=2

for i in range(Last):
    pi1=str(math.pi)
    print(pi1[:2+j])
    j+=1

# Вводится строка из слов, разделенных пробелами. Найти самое длинное слово и вывести его на экран.  task 5

str3=input('Enter a string ')
list_1=str3.split()
list_1.sort(key = len)
print(list_1[-1])

# Напишите программу, которая определит самое короткое слово  task 1+

num_of_strings=int(input('Number of strings '))
w=''

for j in range(num_of_strings):
    str_1=input('String ')
    w1 = ''

    for i in range(len(str_1) + 1):
        w1 = w1 + str_1[i]
        if w1 == str_1[i + 1:i + len(w1) + 1]:
            if len(w) == 0:
                w=w1
            elif len(w) > len(w1):
                w=w1
            break

print('Min word is ',w)

# 2)Напишите программу для  очистки текста от html-тэгов.
# Больше о htmlтэгах https://html5book.ru/html-tags/ Также необходимо учесть пару особенностей:
# - помимо одинарных тэгов, есть парные тэги, например <div> </div>, т.е. первый тэг открывающий ,
# а второй закрывающий. - тэг внутри себя, может содержать кучу доп. информации. Например
# <div id="rcnt" style="clear:both;position:relative;zoom:1">           task 2+

# Note: очистка от тегов и от данных внутри тегов
Text='tqwtqetqewtqewtqe <erwtyerwytr> wewewewewewew1 <wewewe> ewewe2'

str_new=''
t=1
left=0
right=0

while t>0:
    if left > 0:
        right = Text.find('>', left+1)
        left = 0

    elif right > 0 or left ==0 and right<=0:
        left = Text.find('<', right + 1)
        str_new = str_new + Text[right+1:left]
        right=0

    elif left <= 0 and right <= 0:
        str_new = str_new + Text [-1]
        break

print (str_new)



