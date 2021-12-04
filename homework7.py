# Используя словарь, напишите программу,
# которая выведет на экран название дня недели по его номеру.  (1 - «Monday»)       task 1

days={1:'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',5:'Friday', 6:'Saturday',7:'Sunday'}
d=int(input('num of day '))
print(days.get(d))

# Представьте описание кота (домашнее животное) на основе словаря.                  task 2

cats ={'name': 'Tom', 'age': 4, 'color': 'black', 'breed':'brit'}
print (cats)

# Напишите программу которая считает строку текста с клавиатуры и выведет
# на экран статистику, сколько раз какая буква встречается в этой строке.
# Например, для строки «Hello world» эта статистика выглядит,
# как: «H» - 1 , «e» - 1, «l» - 3 и тд.                                             task 3

str1=input('Enter a string ')
dict1={}

for i in str1:
    numb1 = dict1.get(i)
    if numb1:
        dict1[i] = numb1 + 1
    else:
        dict1[i] = 1

print(dict1)




