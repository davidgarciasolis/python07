from abc import ABC, abstractmethod
from .creature import Creature


class CreatureFactory(ABC):
    """Interfaz abstracta para construir criaturas base y evolucionadas."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Crea la forma base de la criatura."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Crea la forma evolucionada de la criatura."""
        pass
