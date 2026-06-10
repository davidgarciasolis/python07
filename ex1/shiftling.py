from ex0.creature import Creature
from .transform_capability import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformado:
            return (f"{self.name} performs a boosted strike!")
        else:
            return (f"{self.name} attacks normally.")

    def transform(self) -> str:
        self.transformado = True
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        self.transformado = False
        return (f"{self.name} returns to normal.")
