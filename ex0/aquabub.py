from .creature import Creature


class Aquabub(Creature):
    """Criatura base de agua."""

    skill: str

    def __init__(self) -> None:
        """Inicializa Aquabub con sus valores por defecto."""
        super().__init__("Aquabub", "Water")
        self.skill = "Water Gun"

    def attack(self) -> str:
        """Devuelve el texto de ataque de Aquabub."""
        return (f"{self.name} uses {self.skill}!")
