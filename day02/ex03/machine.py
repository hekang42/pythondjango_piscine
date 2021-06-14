#!/usr/bin/python3
import random
import beverages

class BrokenMachineException(Exception):
    def __init__(self):
        super().__init__("This coffee machine has to be repaired.")

class CoffeeMachine:
    num_count = 0
    def __init__(self):
        pass
    def repair(self):
        CoffeeMachine.num_count = 0
    def serve(self, cls):
        try: 
            if (CoffeeMachine.num_count >= 10):
                raise BrokenMachineException
            else :
                if random.randrange(0, 100) % 2:
                    print(cls())
                else:
                    print(EmptyCup())
                CoffeeMachine.num_count += 1
        except Exception as e:
            print(e)

class EmptyCup(beverages.HotBeverage):
    def __init__(self):
        self.name = "empty cup"
        self.price = 0.90
    def description(self):
        return "An empty cup?! Gimme my money back!"

def drinkBeverage():
    machine = CoffeeMachine()
    machine.serve(beverages.Chocolate)
    machine.serve(beverages.Chocolate)
    machine.serve(beverages.Chocolate)
    machine.serve(beverages.Chocolate)
    machine.serve(beverages.Chocolate)
    machine.serve(beverages.Chocolate)
    machine.serve(beverages.Chocolate)
    machine.serve(beverages.Chocolate)
    machine.serve(beverages.Chocolate)
    machine.serve(beverages.Coffee)
    machine.serve(beverages.Chocolate)
    machine.serve(beverages.Chocolate)
    machine.repair()
    machine.serve(beverages.Tea)
    machine.serve(beverages.Tea)
    machine.serve(beverages.Tea)
    machine.serve(beverages.HotBeverage)



if __name__ == '__main__':drinkBeverage()