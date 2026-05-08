from .creature import Creature

class Pyrodon(Creature):
    skill:str

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")
        self.skill = "Flamethrower"
    
    def attack(self) -> str:
        return (f"{self.name} uses {self.skill}!")