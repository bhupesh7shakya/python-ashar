class GrandFather:
    def __init__(self) -> None:
        print("grandfather")
    house="house"


class Mother:
    def __init__(self) -> None:
        print("Mother")
    jewellary="gold chain"

class Father(GrandFather):
    def __init__(self) -> None:
        super().__init__()
        print("father")
    color="white"
    car="honda car"
     
    def driving(self):
        print("i can drive car ")
    
class Son(Father,Mother):
    def __init__(self) -> None:
        super().__init__()
        print("son")
    def driving(self):
        super().driving()
        print("i can  fly planes")
        

class Daughter(Mother):
    pass

son=Son()
# print(son.driving())

print(isinstance(son,GrandFather))




# son.driving()




# print(child.color)
# print(son.house)
# son.driving()
# print(son.jewellary)