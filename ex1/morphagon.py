from ex0.creature import Creature
from .transform_capability import TransformCapability


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformado:
            return (f"{self.name} unleashes a devastating morph strike!")
        else:
            return (f"{self.name} attacks normally.")

    def transform(self) -> str:
        self.transformado = True
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        self.transformado = False
        return (f"{self.name} stabilizes its form.")
