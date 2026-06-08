from .creature import Creature


class Flameling(Creature):
    """Criatura base de fuego."""

    skill: str

    def __init__(self) -> None:
        """Inicializa el Flameling con sus valores por defecto."""
        super().__init__("Flameling", "Fire")
        self.skill = "Ember"

    def attack(self) -> str:
        """Devuelve el texto de ataque de Flameling."""
        return (f"{self.name} uses {self.skill}!")
