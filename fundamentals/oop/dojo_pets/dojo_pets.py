import pet

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet= pet
    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print(f"Walking {self.pet.name}")
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() 
    def feed(self):
        print(f"Feeding {self.pet.name}")
        self.pet.eat()
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"Bathing {self.pet.name}")
        self.pet.noise()

stephen = Ninja("Stephen", "Lee", ["jerky", "salad"], "food", pet.Cat("Choco", "cat", "back flip"))
stephen.walk()
stephen.feed()
stephen.bathe()