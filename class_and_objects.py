class Person:
    # name = "ashu"
    # occ = "Data analyst"
    def __init__(self,name,occ):
        self.name = name
        self.occ = occ
    def hello(self):
        print(f"my name is {self.name} and my occupation is {self.occ}")


class Family(Person):



a = Person("rajan","HR")
# print(a.hello()
print(a.name)
a.hello()
