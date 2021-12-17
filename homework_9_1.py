


#Существуют такие последовательности чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реализуйте программу, которая выведет следующий член этой последовательности (либо подобной им) на экран

def seq(*args)->int:
    if (args[1]-args[0])==(args[2]-args[1]):
        return args[len(args)-1]+(args[1]-args[0])
    if (args[1]/args[0])==(args[2]/args[1]):
        return args[len(args)-1]*(args[1]/args[0])
    if args[0]**(1/2)==1 and args[1]**(1/2)==2:
        return (len(args)+1)**2
    if args[0]**(1/3)==1 and args[1]**(1/3)==2:
        return (len(args)+1)**3


print(seq(0,2,4,6,8,10,12))
print(seq(1,4,7,10,13))
print(seq(1,2,4,8,16,32))
print(seq(1,3,9,27))
print(seq(1,4,9,16,25))
print(seq(1,8,27,64,125))


# Самое большое число-палиндром, полученное умножением двух двузначных чисел: 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
# Выведите значение этого палиндрома и то, произведением каких чисел он является.
def polly(a:int,b:int)->int:
    palimax=1
    if not 6>(len(str(a)) + len(str(b)))>4:
        return None
    for i in range(a,b):
        for j in range(a,b):
            palin=str(i*j)
            if palin==palin[-1:-5:-1]:
                palimax=max(int(palin),palimax)
    return palimax

print(polly(10,1))







