from .creature import Creature

class Torragon(Creature):
    skill:str

    def __init__(self) -> None:
        super().__init__("Torragon", "Water")
        self.skill = "Hydro Pump"
    
    def attack(self) -> str:
        return (f"{self.name} uses {self.skill}!")
