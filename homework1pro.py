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
        return f'Name:  {self.name} Price: {self.price}  Decriptiont: {self.description} '


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

    def __repr__(self):
        return str(self.__dict__)

class Order:
    """
    Order of nternet-shop
    """
    def __init__(self, ord_number, order_date, customer: Customer, products=None ):
        self.ord_number=ord_number
        self.order_date=order_date
        self.customer=customer
        self.products=products

    def __str__(self):
        res ='\n'.join(map(str, self.products))
        return f'{self.ord_number} {self.customer}\n{res} \nTotal price :{self.total_price()} UAH '

    def total_price(self):
        s=0
        for item in self.products:
            s += item.price
        return s


if __name__ == '__main__':
    goods1 = Goods('1001', 'phone', 9000, '456', '120', '10', 'Nokia phone....')
    goods2 = Goods('1002', 'phone', 9123 , '340', '100', '8', 'Samsung phone....')
    goods3 = Goods('1003', 'phone', 3213 , '340', '80', '8', 'Xmmx phone....')
    customer1 = Customer('Basil', 'Pupking', '102', 'Basil@gmale.net', 'passw', 'login')
    print(customer1)
    order1 = Order('2341', '01.01.2022', customer1,[goods1,goods2,goods1] )
    order1.products.append(goods3)
    print(order1)




