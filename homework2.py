st='123'                                                    # tasks 1-2
integ=int(st)
fl=float(integ)
print ('integer = ',integ, 'float = ',fl)

integ=int(12.345)                                           # task 3
print ('integer = ',integ)

# Write a Python-script that detects the last 4 digits of a credit card      #task 4
crnumber=input('Enter your card number: ')
last_quarter=crnumber[12:16]
print ('last_quarter = ', last_quarter)


# Write a Python-script that calculates the                  task 5
# sum of the digits of a three-digit numbe
x=123
y=(x//10**2+x//10%10+x%10)
print('sum = ',y)

# Write a program that calculates and displays               task 6
# the area of a triangle if its sides are known
import math
side1=3
side2=4.5
side3=2
perimeter=(side1+side2+side3)/2
square=math.sqrt(perimeter*(perimeter-side1)*(perimeter-side2)*(perimeter-side3))
print('square = ',square)

# 7. *Write a Python-script that calculates the sum of the digits of a number  task 7-8
# 8. *Determine the number of digits in a number
numb=input('Number :' )
str1=str(numb)
l=len(str1)
i=0
s=0
while i<l:
    s=s+int(str1[i])
    i=i+1
print('sum = ',s)
print('digits = ',l)

# *Print the digits in reverse order                                        task 9
i=l
while i>0:
    i=i-1
    print(str1[i])

