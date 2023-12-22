# class : A class is a user-defined data type that represents a blueprint for creating objects. 
# -> It defines a set of properties (attributes) and methods (functions) that the objects created from the class will have.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
# object : An object is an instance of a class. 
# It is a concrete entity created from the class blueprint, and it can store data and perform actions defined by the class
my_car = Car("Toyota", "Camry", 2022)
my_car.display_info()
# Attributes: These are the properties or data members of a class. In the Car class example, make, model, and year are attributes.
# Methods: These are functions defined within a class. 
# ->They represent the behavior or actions that objects created from the class can perform. 
# ->In the Car class example, display_info is a method.
# Inheritance: It refers to the bundling of data (attributes) and the methods that operate on that data within a single unit, i.e., the class
# types of inheritance: []
# single inheritance: 
class father:
    def lands(self):
        print("having 50 acers land")
class son(father):
    def money(self):
        print("Having 10 lacks cash")
m = son()
m.lands()
m.money()
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
# multiple inheritance: inheritance which have two parent classes and one child class is called multiple inheritance
class developer1 :
    front = "HTML,CSS,JavaScript"
    def frontend(self):
        print("frontend development using by: ",self.front)
class developer2 :
    back = "PYTHON,Django"
    def backend(self):
        print("backend development using by: ",self.back)
class teamlead(developer1,developer2) :
    def fullstack(self):
        print("mern stack website development completed")
t = teamlead()
t.frontend()
t.backend()
t.fullstack()
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

# polymorphism: It allows objects of different classes to be treated as objects of a common base class.
#  It enables code reuse and flexibility.
# operator overloading :
class student:
    def __init__(self,m1,m2):
        self.m1 = m1 
        self.m2 = m2 
    def __add__(self,other):
        m1 = self.m1 + other.m1 
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3
    def __gt__(self,other):
        r1 = self.m1 + self.m2 
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True 
        else:
            return False
        
s1 = student(72,69)
s2 = student(80,65)
s3 = s1 + s2 
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")
# overriding: 
class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        print("in B show")
a1 = B()
a1.show()
# super():it is inbuilt method used to call the super()(parent) class constructor,variables,methods from the child(sub)class()
class  Person: 
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def display(self):
        print("name: ",self.name)
        print("age: ",self.age)
class Employee(Person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.emp_id =  emp_id
        self.salary = salary 
    def display(self):
        super().display()
        print("emp_id: ",self.emp_id)
        print("salary: ",self.salary)
e1 = Employee("Ravi",25,"MT-01947",17000)
print(e1)
e1.display()
print(e1)
print(e1.__dict__)

# encapsulation:  It refers to the bundling of data (attributes) and the methods that operate on that data within a single unit, i.e., the class.
 
