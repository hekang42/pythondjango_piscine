#!/usr/bin/python3
class Intern:
    def __init__(self, *args):
        if (len(args) == 0):
            self.Name = "My name? I'm nobody, an intern, I have no name."
        elif (len(args) == 1):
            self.Name = args[0]
        else :
            print("Error Check Argument")
            self.Name = "Too many name"
    def __str__(self):
        return (self.Name)
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
    def make_coffee(self):
        return self.Coffee()


def internParty():
    intern = Intern()
    print(intern.Name)
    Mark = Intern("Mark")
    print(Mark.Name)
    print(Mark.make_coffee())
    try:
        intern.work()
    except Exception as e:
        print(e)

if __name__ == '__main__':internParty()