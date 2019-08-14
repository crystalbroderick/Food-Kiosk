from Order import Order
import datetime

class Receipt():
    def __init__(self, TotalCost):
        self.TotalCost=TotalCost
        self.date=datetime.date.today()

    def getDate(self):
        return self.date

    def __str__(self):
        self.TotalCost=round(self.TotalCost,2)
        response="Total:" + str(self.TotalCost)
        return response