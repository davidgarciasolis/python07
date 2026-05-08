from .creature import Creature

class Aquabub(Creature):
    skill:str

    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")
        self.skill = "Water Gun"
    
    def attack(self) -> str:
        return (f"{self.name} uses {self.skill}!")
