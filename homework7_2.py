# Ввести с клавиатуры число (до миллиона), которое обозначает количество долларов и центов пользователя.
# Вывести это количество прописью

NUMBERS = { 10 : ' ten ',
           11:'eleven',
           12:'twelve',
           13:'thirteen',
           14:'fourteen',
           15:'fifteen',
           16:'sixteen',
           17:'seventeen',
           18:'eigteen',
           19:'nineteen',
           20:'twenty',
           30:'thirty',
           40:'fourty',
           50:'fifty',
           60:'sixty',
           70:'seventy',
           80: 'eighty',
           90:'ninety',
           1:'one',
           2:'two',
           3:'three',
           4:'four',
           5:'five',
           6:'six',
           7:'seven',
           8:'eight',
           9:'nine',
           }
NUMB1={0:'hundred ',
       1: '',
       2: 'thousand ',
       3: 'hundred ',
       4: '',
       5: 'dollar',
       6: '',
       7:'',
       8: 'cent'}
nat='341232,56'
stro=''
j=0
for i in nat:
    if i!='0' and i!=',':
        if not (j-1)%3:
            stro = stro +  NUMBERS.get(int(nat[j] + '0'))
        else:
            stro = stro +  NUMBERS.get(int(nat[j]))

    stro = stro  + ' '+ NUMB1.get(j)
    j+=1

print(stro)

