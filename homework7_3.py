# Напишите программу, которая переведет целое число (от 1 до 100) из римской записи в  обычные цифры.
# Например: XXII  ->  22

ROMA = { 'X': 10,
         'XX': 20,
         'XXX': 30,
         'XL':40,
         'L':50,
         'LX':60,
         'LXX': 70,
         'LXXX':80,
         'XC':90,
          'C':100,
         'I':1,
         'II' :2,
         'III' :3,
         'IV' :4,
         'V':5,
         'VI':6,
         'VII':7,
         'VIII' : 8,
         'IX' :9
           }
qq=0
q='XXXIX'
j=0
while True:
    if q[j]!='I' and q[j]!='V':
        qq=qq+ROMA.get(q[j])
    else:
        qq = qq + ROMA.get(q[j:len(q)])
        break
    j+=1

print (qq)







