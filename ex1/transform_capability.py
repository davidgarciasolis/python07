from abc import ABC, abstractmethod


class TransformCapability(ABC):
    """Interfaz para criaturas que pueden transformarse y revertir."""

    transformado: bool

    def __init__(self) -> None:
        """Inicializa el estado de transformación en falso."""
        self.transformado = False

    @abstractmethod
    def transform(self) -> str:
        """Activa la transformación y devuelve su descripción."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Revierte la transformación y devuelve su descripción."""
        pass
