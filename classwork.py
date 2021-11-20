oc=int(input('oc '))
if oc > 100:
    print('Error!')
elif oc > 90:
    print ('A')
elif oc > 80:
    print('B')
elif oc> 70:
    print('C')
elif oc > 60:
    print('D')
elif oc > 50:
    print('E')
elif 50 > oc:
    print('F')

#...x is odd
#...x is a multiple of 20 (e.g., 20, 40, 60, ...)

x,y,z=(20,20,20)
if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
    print("all the numbers are integers")
    if x%2:
        print('x is not odd')
    else:
        print('x is odd')
    if x//20 > 0:
        print ('x is multiple of 20= ',x)
    else:
        print('x is not multiple of 20= ', x)

#...x and y are both positive

if x>=0 and y>=0:
    print ('both are positive')
else:
    print ('one of x,y is negative')

#...x and y have the same sign (both are positive or both are negative)

if x>=0 and y>=0 or x<0 and y<0:
    print('x and y have the same signs')
else:
    print('x and y have different signs')

#...all three names (x, y, and z) are bound to equal values
#...all three names (x, y, and z) are bound to different values (none the same)
#...two variables store the same value, but the third one is different

if x==y==z:
    print('(x, y, and z) are bound to equal values')
elif x==y or y==z or x==z:
    print('two variables store the same value')
else:
    print('(x, y, and z) are bound to different values')

