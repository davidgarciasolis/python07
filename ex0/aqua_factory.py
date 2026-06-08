from .creature_factory import CreatureFactory
from .creature import Creature
from .aquabub import Aquabub
from .torragon import Torragon


class AquaFactory(CreatureFactory):
    """Fábrica que construye criaturas de tipo agua."""

    def create_base(self) -> Creature:
        """Crea la criatura base acuática."""
        return (Aquabub())

    def create_evolved(self) -> Creature:
        """Crea la criatura acuática evolucionada."""
        return (Torragon())
