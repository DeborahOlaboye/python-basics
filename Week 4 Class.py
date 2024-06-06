class Dog:
    __number = 0
    # _protected = "I am a protected variable"
    def __init__(self, name):
        self.name = name
        Dog.__number += 1
        self.dognumber = Dog.__number

    

    def bark(self):
        print(f"{self.name} says woof!")
    
jack = Dog("Jack")
print(f"{jack.dognumber}")