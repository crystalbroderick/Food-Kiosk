from OrderItem import OrderItem
from MenuItems import MenuItems

class Order():
    def __init__(self):
        self.orderitem=[]

    def addOrderItems(self, OrderItem):
        self.orderitem.append(OrderItem)

    def getOrderItem(self):
        return self.orderitem

    def TotalCost(self):
        total=0.0
        for o in self.orderitem:
            total += o.getMenuItem().Price * o.quantity
        return total