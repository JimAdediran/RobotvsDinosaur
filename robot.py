from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("sword", 30)
    def attack(self, dinosaur):
        self.dinosaur = dinosaur
        self.dinosaur -= self.active_weapon.attack_power
        pass