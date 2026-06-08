from ex0.creature import Creature
from .heal_capability import HealCapability


class Sproutling(Creature, HealCapability):
    """Criatura base con capacidad de curación."""

    skill: str

    def __init__(self) -> None:
        """Inicializa Sproutling con sus valores por defecto."""
        super().__init__("Sproutling", "Grass")
        self.skill = "Vine Whip"

    def attack(self) -> str:
        """Devuelve el texto de ataque de Sproutling."""
        return (f"{self.name} uses {self.skill}!")

    def heal(self) -> str:
        """Devuelve el texto de curación de Sproutling."""
        return (f"{self.name} heals itself for a small amount")
