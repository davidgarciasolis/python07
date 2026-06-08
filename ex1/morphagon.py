from ex0.creature import Creature
from .transform_capability import TransformCapability


class Morphagon(Creature, TransformCapability):
    """Criatura evolucionada capaz de transformarse."""

    skill: str

    def __init__(self) -> None:
        """Inicializa Morphagon y su estado de transformación."""
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)
        self.skill = "normally"

    def attack(self) -> str:
        """Devuelve el texto de ataque según el estado actual."""
        if self.transformado:
            return (f"{self.name} unleashes a devastating morph strike!")
        else:
            return (f"{self.name} uses {self.skill}!")

    def transform(self) -> str:
        """Activa la forma de combate de Morphagon."""
        self.transformado = True
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        """Devuelve a Morphagon a su forma estable."""
        self.transformado = False
        return (f"{self.name} stabilizes its form.")
