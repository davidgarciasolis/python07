from .creature import Creature


class Pyrodon(Creature):
    """Criatura evolucionada de fuego."""

    skill: str

    def __init__(self) -> None:
        """Inicializa Pyrodon con sus valores por defecto."""
        super().__init__("Pyrodon", "Fire/Flying")
        self.skill = "Flamethrower"

    def attack(self) -> str:
        """Devuelve el texto de ataque de Pyrodon."""
        return (f"{self.name} uses {self.skill}!")
