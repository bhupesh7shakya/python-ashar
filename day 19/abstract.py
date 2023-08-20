from abc import ABC,abstractmethod

class Computer(ABC):
    
    @abstractmethod
    def process(self,name):
        pass
    
    def run(self,name):
        self.process(name)

class Laptop(Computer):
    
    def process(self,name):
        print(f"{name} is running on laptop")


class Mobile(Computer):
    def process(self,name):
        print(f"{name} is running on mobile")
        
        
laptop=Laptop()
laptop.run("chrome")
laptop.run("pubg")
laptop.run("music player")
laptop.run("vs-code")


mobile=Mobile()
mobile.run("pubg")