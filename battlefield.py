from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.robot = Robot('John')
        self.dinosaur = Dinosaur('Kyle', 30)

    def run_game(self):
        self.display_welcome()
            
        self.battle_phase()
            
        self.display_winner()
        

    def display_welcome(self):
        print("Welcome ot an epic battle for the ages!")
        print("Only one side can win!")
    
    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            Robot.attack(self.dinosaur.health)
            print(f'{self.robot.name} attacked {self.dinosaur.name} for {self.robot.active_weapon.attack_power} damage!')
            print(f'{self.dinosaur.name} has {self.dinosaur.health} remaining!')
            Dinosaur.attack(self.robot.health)
            print(f'{self.dinosaur.name} attacked {self.robot.name} for {self.dinosaur.attack_power} damage!')
            print(f'{self.robot.name} has {self.robot.health} remaining!')

    def display_winner(self):
        if Robot.health <= 0:
            print(f'{Dinosaur} made {Robot} extinct!')
            print(f'{Dinosaur} wins!')
        else:
            print(f'{Robot} made {Dinosaur} extinct!')
            print(f'{Robot} wins!')
            pass
