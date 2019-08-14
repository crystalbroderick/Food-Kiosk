from Menu import Menu

class MenuItems():
    def __init__(self, MenuItemNum, MenuItemName, Price):
        self.MenuItemNum=MenuItemNum
        self.MenuItemName=MenuItemName
        self.Price=Price
    
    def getMenuItemNum(self):
        return self.MenuItemNum

    def getMenuItemName(self):
        return self.MenuItemName

    def getPrice(self):
        return self.Price

    def addPrice(self):
        return

    def __str__(self):
        return self.MenuItemName