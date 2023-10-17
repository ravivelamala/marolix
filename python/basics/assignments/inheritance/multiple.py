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