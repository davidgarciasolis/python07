from .creature import Creature


class Flameling(Creature):
    skill: str

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")
        self.skill = "Ember"

    def attack(self) -> str:
        return (f"{self.name} uses {self.skill}!")
