from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (AggressiveStrategy, DefensiveStrategy,
                 NormalStrategy, BattleStrategy,
                 ErrorStrategy)


def battle(first_oponent: tuple[CreatureFactory, BattleStrategy],
           second_oponent: tuple[CreatureFactory, BattleStrategy]
           ) -> None:

    first_creature = first_oponent[0].create_base()
    second_creature = second_oponent[0].create_base()

    print("* Battle *")
    print(first_creature.describe())
    print(" vs.")
    print(second_creature.describe())
    first_oponent[1].act(first_creature)
    second_oponent[1].act(second_creature)
    print()


def Tournament(oponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    num_oponents = len(oponents)

    print("*** Tournament ***")
    print(f"{num_oponents} opponents involved")
    print()
    for x in range(num_oponents):
        y = x + 1
        while y < num_oponents:
            battle(oponents[x], oponents[y])
            y += 1


def main() -> None:
    flame_factory = FlameFactory()
    aqua_Factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()
    normal_strategy = NormalStrategy()

    oponents1 = [(flame_factory, normal_strategy),
                 (healing_factory, defensive_strategy)]
    oponents2 = [(flame_factory, aggressive_strategy),
                 (healing_factory, defensive_strategy)]
    oponents3 = [(aqua_Factory, normal_strategy),
                 (healing_factory, defensive_strategy),
                 (transform_factory, aggressive_strategy)]

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    try:
        Tournament(oponents1)
    except ErrorStrategy as e:
        print(f"Battle error, aborting tournament: {e}")
        print()

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    try:
        Tournament(oponents2)
    except ErrorStrategy as e:
        print(f"Battle error, aborting tournament: {e}")
        print()

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    try:
        Tournament(oponents3)
    except ErrorStrategy as e:
        print(f"Battle error, aborting tournament: {e}")
        print()


if __name__ == "__main__":
    main()
