
from ex0 import CreatureFactory, AquaFactory, FlameFactory


def testing_factory(creature_factory:CreatureFactory) -> None:
    creature_base = creature_factory.create_base()
    creature_evolved = creature_factory.create_evolved()

    print("Testing factory")
    print(creature_base.describe())
    print(creature_base.attack())
    print(creature_evolved.describe())
    print(creature_evolved.attack())
    print()

def testing_battle(creature_factory_first:CreatureFactory, creature_factory_second:CreatureFactory) -> None:
    creature_first = creature_factory_first.create_base()
    creature_second = creature_factory_second.create_base()

    print("Testing battle")
    print(creature_first.describe())
    print(" vs.")
    print(creature_second.describe())
    print(" fight!")
    print(creature_first.attack())
    print(creature_second.attack())
    print()

def main() -> None:
    flame_factory = FlameFactory()
    aqua_Factory = AquaFactory()

    testing_factory(flame_factory)
    testing_factory(aqua_Factory)
    testing_battle(flame_factory, aqua_Factory)


if __name__ == "__main__":
    main()
