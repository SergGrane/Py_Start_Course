# СОЗДАТЬ СПИСОК 5 КОТОВ С ИМЕНЕМ И ВОЗРАСТОМ, ИСПОЛЬЗУЯ СЛОВАРЬ. ОПРЕДЕЛИТЬ ВОЗРАСТ СТАРЕЙШЕГО КОТА

i=0
cats=[]
ma=0
while i<5:
    nam=input('cat_name ')
    ag=int(input('age '))
    cat={'name':nam, 'age' :  ag}
    ma=max(ma,cat.get('age'))
    cats.append(cat)
    print (cat)
    i=i+1

print(cats)
print('max_age =', ma)