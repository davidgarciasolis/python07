from ex0.creature import Creature
from .heal_capability import HealCapability


class Bloomelle(Creature, HealCapability):
    """Criatura evolucionada con capacidad de curación."""

    skill: str

    def __init__(self) -> None:
        """Inicializa Bloomelle con sus valores por defecto."""
        super().__init__("Bloomelle", "Grass")
        self.skill = "Vine Whip"

    def attack(self) -> str:
        """Devuelve el texto de ataque de Bloomelle."""
        return (f"{self.name} uses {self.skill}!")

    def heal(self, target: str = "others") -> str:
        """Devuelve el texto de curación de Bloomelle."""
        return (f"{self.name} heals itself and {target} for a large amount")
