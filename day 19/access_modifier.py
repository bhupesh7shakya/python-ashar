class Person:
    def __init__(self,name,age,password):
        # public
        self.name=name
        # protected
        self._age=age
        # private
        self.__password=password
        
    def get_password(self):
        return self.__password
    
    def set_password(self,password):
        self.__password=password
        
    
        
person=Person("ram",13,1234)
print(person.name)
print(person._age)
person.set_password(9876)
print(person.get_password())