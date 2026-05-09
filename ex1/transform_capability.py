from abc import ABC, abstractmethod


class TransformCapability(ABC):
    transformado: bool

    def __init__(self) -> None:
        self.transformado = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
