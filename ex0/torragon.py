from .creature import Creature


class Torragon(Creature):
    """Criatura evolucionada de agua."""

    skill: str

    def __init__(self) -> None:
        """Inicializa Torragon con sus valores por defecto."""
        super().__init__("Torragon", "Water")
        self.skill = "Hydro Pump"

    def attack(self) -> str:
        """Devuelve el texto de ataque de Torragon."""
        return (f"{self.name} uses {self.skill}!")
