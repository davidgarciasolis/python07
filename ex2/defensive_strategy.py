from .battle_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.heal_capability import HealCapability


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.name = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return (True)
        else:
            return (False)

    def act(self, creature: Creature) -> None:
        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())
        else:
            raise Exception(f"Invalid Creature '{creature.name}' "
                            f"for this {self.name} strategy")
