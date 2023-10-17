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