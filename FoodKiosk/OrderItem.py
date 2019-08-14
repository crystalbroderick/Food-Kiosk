from MenuItem import MenuItem

class OrderItem():
    def __init__(self, MenuItem, Quantity):
        self.MenuItem=MenuItem
        self.Quantity=Quantity

    def getMenuItem(self):
        return self.MenuItem

    def getQuantity(self):
        return self.Quantity