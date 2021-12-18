class Goods:
    """
    Goods from internet-shop
    """
    num_of_goods=0
    def __init__(self, partnumber, name , price, weight, height, width, description):
        self.partnumber=partnumber
        self.name=name
        self.price=price
        self.weight=weight
        self.height=height
        self.width=width
        self.description=description


    def __str__(self):
        return f'Name:  {self.name} Price: {self.price}  Decriptiont: {self.description} {self.num_of_goods}'

class Customer:
    """
    Customer of internet-shop
    """
    def __init__(self, name, surname, phone_number, mail, passw, login):
        self.name=name
        self.surname=surname
        self.phone_number=phone_number
        self.mail=mail
        self.passw=passw
        self.login=login

    def __str__(self):
        return f'Name:  {self.name}  {self.surname}  Phone number: {self.phone_number} E-mail: {self.mail}'

class Order:
    """
    Order of nternet-shop
    """
    def __init__(self, ord_number, order_date, cust_name, cust_surname, address, goods_and_q_ty: list):
        self.ord_number=ord_number
        self.order_date=order_date
        self.cust_name=cust_name
        self.cust_surname=cust_surname
        self.address=address
        self.goods_and_q_ty=goods_and_q_ty

    def __str__(self):
        res = '\n'.join(map(str, self.goods_and_q_ty))
        return f'Order number: {self.ord_number}, Order date: {self.order_date}, Customer name: {self.cust_name}, {self.cust_surname}, Delivery address: {self.address} ' \
               f'\nPart number & quality:\n{res}'

list_g = []

goods1 = Goods('1001', 'phone', 9000, '456', '120', '10', 'Nokia phone....')
Goods.num_of_goods+=1
list_g.append(goods1.__dict__)
goods2 = Goods('1002', 'phone', 9123 , '340', '100', '8', 'Samsung phone....')
Goods.num_of_goods+=1
list_g.append(goods2.__dict__)
goods3 = Goods('1003', 'phone', 3213 , '340', '80', '8', 'Xmmx phone....')
Goods.num_of_goods+=1
list_g.append(goods3.__dict__)

customer1 = Customer('Basil', 'Pupking', '102', 'Basil@gmale.net', 'passw', 'login')


order1 = Order('2341', '01.01.2022', 'Basil', 'Pupking', 'Petrovka 38', [('1001', 1), ('1002', 2)])

sum=0

for j in order1.goods_and_q_ty :
    for i in list_g:
        if j[0]==i.get('partnumber'):
            sum = sum+ j[1]*i.get('price')

print('Sum of the order :', sum, ' UAH')
