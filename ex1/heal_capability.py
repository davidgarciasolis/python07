from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Interfaz para criaturas que pueden curarse."""

    @abstractmethod
    def heal(self) -> str:
        """Devuelve el texto que describe la curación."""
        pass
