class Animal:
    def __init__(self, name, no_of_legs):
        self.name = name
        self.no_of_legs = no_of_legs

    def get_no_of_legs(self):
        return self.no_of_legs

class Dress:
    def __init__(self, dress_type):
        self.dress_type = dress_type

class Bird(Animal):
    def __init__(self, name, no_of_legs, can_fly):
        super().__init__(name, no_of_legs)
        self.can_fly = can_fly
    
    def get_can_fly(self):
        return self.get_no_of_legs

duck = Bird('Tom', 2, True)
print(duck.name)
print(duck.get_can_fly())