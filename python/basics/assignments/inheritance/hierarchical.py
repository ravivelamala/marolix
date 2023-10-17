# hierarchical inheritance: multiple child classes and one parent class but each child classes can access the parent class
class father():
    surname = "singh"
    def show(self):
        print("my surname is:  ",self.surname)
class son1(father):
    def show1(self):
        print("my name is: akash ",self.surname)
class son2(father):
    def show2(self):
        print("my name is: rajesh ",self.surname)
obj1 = son1()
obj2 = son2()
obj1.show()
obj1.show1()
obj2.show()
obj2.show2()
