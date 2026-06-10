from .battle_strategy import BattleStrategy
from .error_strategy import ErrorStrategy
from ex0.creature import Creature


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.name = "normal"

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return (True)
        else:
            return (False)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise ErrorStrategy(f"Invalid Creature '{creature.name}' "
                                f"for this {self.name} strategy")
