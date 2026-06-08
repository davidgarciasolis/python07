from .battle_strategy import BattleStrategy
from .error_stategy import ErrorStrategy
from ex0.creature import Creature


class NormalStrategy(BattleStrategy):
    """Estrategia básica que permite atacar a cualquier criatura."""

    def __init__(self) -> None:
        """Inicializa el nombre de la estrategia."""
        self.name = "normal"

    def is_valid(self, creature: Creature) -> bool:
        """Comprueba si la criatura es válida para esta estrategia."""
        if isinstance(creature, Creature):
            return (True)
        else:
            return (False)

    def act(self, creature: Creature) -> None:
        """Ejecuta un ataque simple."""
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise ErrorStrategy(f"Invalid Creature '{creature.name}' "
                                f"for this {self.name} strategy")
