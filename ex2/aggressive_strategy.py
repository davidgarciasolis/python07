from .battle_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.transform_capability import TransformCapability


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.name = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return (True)
        else:
            return (False)

    def act(self, creature: Creature) -> None:
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise Exception(f"Invalid Creature '{creature.name}' "
                            f"for this {self.name} strategy")
