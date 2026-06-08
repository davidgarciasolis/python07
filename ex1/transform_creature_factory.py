from ex0 import CreatureFactory
from .shiftling import Shiftling
from .morphagon import Morphagon


class TransformCreatureFactory(CreatureFactory):
    """Fábrica que crea criaturas con capacidad de transformación."""

    def create_base(self) -> Shiftling:
        """Crea la criatura base transformable."""
        return (Shiftling())

    def create_evolved(self) -> Morphagon:
        """Crea la criatura transformable evolucionada."""
        return (Morphagon())
