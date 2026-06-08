from .creature_factory import CreatureFactory
from .creature import Creature
from .flameling import Flameling
from .pyrodon import Pyrodon


class FlameFactory(CreatureFactory):
    """Fábrica que construye criaturas de tipo fuego."""

    def create_base(self) -> Creature:
        """Crea la criatura base de fuego."""
        return (Flameling())

    def create_evolved(self) -> Creature:
        """Crea la criatura de fuego evolucionada."""
        return (Pyrodon())
