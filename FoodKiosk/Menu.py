from MenuItems import MenuItems

class Menu():
    def __init__(self):
        self.MenuItems=[]

    def addMenuItem(self, i):
        self.MenuItems.append(i)

    def getMenuItems(self):
        return self.MenuItems

    def getMenuItemByNum(self, number):
        reqItem=None
        for i in self.MenuItems:
            if i.MenuItemID==number:
                reqItem=i
                break
        return reqItem