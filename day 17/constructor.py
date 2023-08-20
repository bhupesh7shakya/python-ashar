class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def set_name(self,name):
        self.name=name
    
    
    def set_age(self,age):
        self.name=age
    
    def get_name(self):
        return self.name


    def get_age(self):
        return self.age
    
    def __str__(self):
        return self.name
        
person=Person("ram",12)


# print(person)
# # person.age=33
# person.set_name("shyam")
# print(person.get_name())
# # print(person.get_age())


# print("test".__eq__("est"))