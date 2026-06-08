from ex0.creature import Creature
from .transform_capability import TransformCapability


class Shiftling(Creature, TransformCapability):
    """Criatura base capaz de transformarse."""

    skill: str

    def __init__(self) -> None:
        """Inicializa Shiftling y su estado de transformación."""
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)
        self.skill = "normally"

    def attack(self) -> str:
        """Devuelve el texto de ataque según el estado actual."""
        if self.transformado:
            return (f"{self.name} performs a boosted strike!")
        else:
            return (f"{self.name} uses {self.skill}!")

    def transform(self) -> str:
        """Activa la forma transformada de Shiftling."""
        self.transformado = True
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        """Devuelve a Shiftling a su forma normal."""
        self.transformado = False
        return (f"{self.name} returns to normal.")
