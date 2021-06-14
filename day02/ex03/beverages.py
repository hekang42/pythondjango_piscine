#!/usr/bin/python3
class HotBeverage:
    name = "hot beverage"
    price = 0.30
    def description(self):
        return "Just some hot water in a cup"
    def __str__(self):
        return "name : " + self.name + "\n"\
             + "price : " +  format(self.price, ".2f") + "\n"\
             + "description : " + self.description()

class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    name = "tea"

class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    name = "Cappuccino"
    price = 0.45
    def description(self):
        return "Un po' di Italia nella sua tazza!"

def drinkBeverage():
    hotHot = HotBeverage()
    print(hotHot)
    coffee = Coffee()
    print(coffee)
    tea = Tea()
    print(tea)
    chocolate = Chocolate()
    print(chocolate)
    cappuccino = Cappuccino()
    print(cappuccino)

if __name__ == '__main__':drinkBeverage()