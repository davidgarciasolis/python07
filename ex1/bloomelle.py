from ex0.creature import Creature
from .heal_capability import HealCapability


class Bloomelle(Creature, HealCapability):
    skill: str

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")
        self.skill = "Petal Dance"

    def attack(self) -> str:
        return (f"{self.name} uses {self.skill}!")

    def heal(self, target: str = "others") -> str:
        return (f"{self.name} heals itself and {target} for a large amount")
