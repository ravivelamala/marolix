# multilevel inheritance: multiple child classes and one parent class 
class father:
    surname = "singh"
class son(father):
    def show1(self):
        print("akash",self.surname)
class grandson(son):
    def show2(self):
        print("rahul",self.surname)
g = grandson()
g.show1()
g.show2()