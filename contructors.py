class Person:

    def __init__(self,n,o):
        self.name= n
        self.occ = o
        print("I am running")
    def hello(self):
        print(f"my name is {self.name} and my occupation is {self.occ}")


a = Person("Ashu","Data Analyst")
# a.name = "ram"
# a.occ = "HR"
# # print(a.hello())
a.hello()

