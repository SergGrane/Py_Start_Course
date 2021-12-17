# Напишите функцию, которая вернет максимальное число из списка чисел.
def maxx(*args)->int:
    maxi=None
    for item in args:
        if isinstance(item,(int,float)):
            maxi=(item if maxi==None else max(maxi, item))
    return maxi

print (maxx(1,2.5,3,50,8,'ww'))

# Реализуйте функцию, параметрами которой являются - два числа и строка. Возвращает она конкатенацию строки с суммой чисел.

def concat(a:int,b:int,st:str)->str:
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(st,str):
        return ''
    else:
        return str(a+b)+st

print (concat(1,2,'4'))

# Реализуйте функцию рисующую на экране прямоугольник из звездочек «*».
# Ее параметрами будут целые числа, которые описывают длину и ширину такого прямоугольника.

def square(a:int,b:int)->str:
    middle='*'+' '*(a-2) + '*\n'
    sq='*'* a +'\n' + middle*(b-2) + '*'* a
    return sq

print(square(5,5))

#  Напишите функцию, которая реализует линейный поиск элемента в списке целых чисел.
#  Если такой элемент в списке есть, то верните его индекс, если нет, то верните число «-1».

def search(*args,a=0):
    j=0
    res=-1
    #res=args.find(a)
    for i in args:
        if i==a:
            res=i
            return (res,j)
        j+=1
    return res

print (search (1,2,3,'d',8,'we',a=3) )

#  Напишите функцию, которая вернет количество слов в строке текста

import string



def number_of_words(st:str) ->int:
    st1=['!', '"', '#', '$', '%', '&', '(',  ')','*','+',  '-', '.', '/',',']
    for item in st1:
        st=st.replace(item,' ')

    return len(st.split())

print(number_of_words('qwqwqw wewewe we,,,,,ererer  ... errrr ....rerre'))




