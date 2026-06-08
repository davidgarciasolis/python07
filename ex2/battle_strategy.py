from abc import ABC, abstractmethod
from ex0.creature import Creature


class BattleStrategy(ABC):
    """Interfaz abstracta para estrategias de combate."""

    name: str

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Indica si una criatura puede usar esta estrategia."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Ejecuta la acción de combate sobre una criatura."""
        pass
