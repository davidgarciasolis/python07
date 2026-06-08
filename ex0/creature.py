from abc import ABC, abstractmethod


class Creature(ABC):
    """Clase base abstracta para todas las criaturas."""

    name: str
    type: str

    def __init__(self, name: str, type: str) -> None:
        """Inicializa el nombre y el tipo de la criatura."""
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        """Devuelve el texto que describe el ataque de la criatura."""
        pass

    def describe(self) -> str:
        """Devuelve una descripción legible de la criatura."""
        return (f"{self.name} is a {self.type} type Creature")
