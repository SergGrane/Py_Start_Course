# С помощью циклов вывести на экран все простые числа от 1 до 100.
# Простое число — число, которое делится нацело только на единицу или само на себя.
# Первые простые числа это — 2,3,5,7…

FIRST_N=1
LAST_N=100


for i in range(FIRST_N,LAST_N):
    i+=1
    print('i ' ,i)
    j=2
    while j<i:
        if i%j==0 :
            print('not')
            break
        j+=1
    else:
        print('yes')


# Выведите на экран «песочные часы», максимальная ширина которых считывается с клавиатуры (число нечетное).
# В примере ширина равна 5.
# *****
# ***
#  *
# ***
# *****

Width=7
concat=''

for i in range(Width) :

    if i<=Width/2:
        concat=' ' * i+ '*'*(Width-i*2)
        print (concat)

concat=''

for i in range(Width,-1,-1) :

    if i<=Width/2:
        concat = ' ' * i + '*' * (Width - i * 2)
        print(concat)


# Написать код для зеркального переворота списка [7,2,9,4] -> [4,9,2,7].
# Список может быть произвольной длины.

list_1 = list(input('Number '))
len_1=len(list_1)
print(list_1)
i=0
x=' '

while i < len_1//2:
    x=list_1[i]
    list_1[i] = list_1[len_1-1-i]
    list_1[len_1 - 1 - i] = x
    i+=1

print(list_1)