#def decodeBits(bits)
bits='1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
q1=bits.split('00000000000000')
print (q1)

s2=''
for i in q1:
    a1=i.split('000000')
    print(a1)
    for j in a1:
        dot=0
        dash=0
        pos=0
        j1 = j.split('00')
        print('dot ', dot, 'dash', dash, 'j' ,j,j1)
        for x in j1:
            if x == '11':
                s2= s2 + '.'
            else:
                s2 = s2 + '-'

        s2= s2 + ' '
    s2=s2 + '   '


print(s2)

