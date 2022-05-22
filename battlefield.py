from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.robot = Robot('JRobot')
        self.dinosaur = Dinosaur('KDinosaur', 20)

    def run_game(self):
        self.display_welcome()
            
        self.battle_phase()
            
        self.display_winner()
        

    def display_welcome(self):
        print("Welcome to an epic battle for the ages!")
        print("Only one side can win!")
    
    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)
                print(f'{self.robot.name} attacked {self.dinosaur.name} for {self.robot.active_weapon.attack_power} damage!')
                print(f'{self.dinosaur.name} has {self.dinosaur.health} remaining!')
            if self.dinosaur.health >0:
                self.dinosaur.attack(self.robot)
                print(f'{self.dinosaur.name} attacked {self.robot.name} for {self.dinosaur.attack_power} damage!')
                print(f'{self.robot.name} has {self.robot.health} remaining!')

    def display_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} made {self.robot.name} extinct!')
            print(f'{self.dinosaur.name} wins!')
        else:
            print(f'{self.robot.name} made {self.dinosaur.name} extinct!')
            print(f'{self.robot.name} wins!')
            pass
