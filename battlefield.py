from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.robot = Robot('John')
        self.dinosaur = Dinosaur('Kyle', 30)

    def run_game(self):
            def display_welcome():
                def battle_phase():
                    def display_winner():
                        pass

    def display_welcome(self):
        print("Welcome ot an epic battle for the ages!")
        print("Only one side can win!")
    
    def battle_phase(self):
        while Robot.health > 0 and Dinosaur.heath > 0:
            Robot.attack
            print(f'{Robot} attacked {Dinosaur} for {Weapon.attack_power} damage!')
            print(f'{Dinosaur} has {Dinosaur.health} remaining!')
            Dinosaur.attack
            print(f'{Dinosaur} attacked {Robot} for {Dinosaur.attack_power} damage!')
            print(f'{Robot} has {Robot.health} remaining!')

    def display_winner(self):
        if Robot.health <= 0:
            print(f'{Dinosaur} made {Robot} extinct!')
            print(f'{Dinosaur} wins!')
        else:
            print(f'{Robot} made {Dinosaur} extinct!')
            print(f'{Robot} wins!')
            pass
