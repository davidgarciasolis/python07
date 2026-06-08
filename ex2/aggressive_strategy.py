from .battle_strategy import BattleStrategy
from .error_stategy import ErrorStrategy
from ex0.creature import Creature
from ex1.transform_capability import TransformCapability


class AggressiveStrategy(BattleStrategy):
    """Estrategia que exige criaturas transformables."""

    def __init__(self) -> None:
        """Inicializa el nombre de la estrategia."""
        self.name = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        """Comprueba si la criatura puede transformarse."""
        if isinstance(creature, TransformCapability):
            return (True)
        else:
            return (False)

    def act(self, creature: Creature) -> None:
        """Transforma, ataca y revierte la criatura."""
        if self.is_valid(creature):
            if (isinstance(creature, TransformCapability)):
                print(creature.transform())
                print(creature.attack())
                print(creature.revert())
        else:
            raise ErrorStrategy(f"Invalid Creature '{creature.name}' "
                                f"for this {self.name} strategy")
