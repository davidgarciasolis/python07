from ex0 import CreatureFactory
from .sproutling import Sproutling
from .bloomelle import Bloomelle


class HealingCreatureFactory(CreatureFactory):
    """Fábrica que crea criaturas con capacidad de curación."""

    def create_base(self) -> Sproutling:
        """Crea la criatura base curativa."""
        return (Sproutling())

    def create_evolved(self) -> Bloomelle:
        """Crea la criatura curativa evolucionada."""
        return (Bloomelle())
