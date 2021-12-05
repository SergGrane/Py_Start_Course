

# 2)Напишите программу для  очистки текста от html-тэгов.
# Больше о htmlтэгах https://html5book.ru/html-tags/ Также необходимо учесть пару особенностей:
# - помимо одинарных тэгов, есть парные тэги, например <div> </div>, т.е. первый тэг открывающий ,
# а второй закрывающий. - тэг внутри себя, может содержать кучу доп. информации. Например
# <div id="rcnt" style="clear:both;position:relative;zoom:1">           task 2+
#text = 'qwqwqwqwqqwqwq'
text = ''' <head>  <link rel="stylesheet" href="/lib/w3schools30.css"> <title>Python String Methods</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="Keywords" content="HTML, Python, CSS, SQL, JavaScript, How to, PHP, Java, C++, jQuery, Bootstrap, C#, Colors, W3.CSS, XML, MySQL, Icons, NodeJS, React, Graphics, Angular, R, AI, Git, Data Science, Code Game, Tutorials, Programming, Web Development, Training, Learning, Quiz, Courses, Lessons, References, Examples, Source code, Demos, Tips">
<meta name="Description" content="Well organized and easy to understand Web building tutorials with lots of examples of how to use HTML, CSS, JavaScript, SQL, Python, PHP, Bootstrap, Java, XML and more.">
<meta property="og:image" content="https://www.w3schools.com/images/w3schools_logo_436_2.png"> '''

str_new=''
left=0
right=0

while True :
    if left > 0:
        right = text.find('>', left + 1)
        left = 0

    elif right > 0 or left ==0 and right == 0:
        left = text.find('<', right + 1)
        str_new = str_new + text[right+1:left]
        right=0

    elif left <= 0 and right <= 0:
        str_new = str_new + text [-1]
        break

print (str_new)



