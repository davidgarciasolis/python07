from ex0.creature import Creature
from .heal_capability import HealCapability


class Sproutling(Creature, HealCapability):
    skill: str

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")
        self.skill = "Vine Whip"

    def attack(self) -> str:
        return (f"{self.name} uses {self.skill}!")

    def heal(self) -> str:
        return (f"{self.name} heals itself for a small amount")
