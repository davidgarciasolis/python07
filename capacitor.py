from ex1 import HealingCreatureFactory, TransformCreatureFactory


def testing_creature_heal() -> None:
    healing_factory = HealingCreatureFactory()
    creature_base = healing_factory.create_base()
    creature_evolved = healing_factory.create_evolved()

    print(" base:")
    print(creature_base.describe())
    print(creature_base.attack())
    print(creature_base.heal())
    print(" evolved:")
    print(creature_evolved.describe())
    print(creature_evolved.attack())
    print(creature_evolved.heal())
    print()


def testing_creature_transform() -> None:
    transform_factory = TransformCreatureFactory()
    creature_base = transform_factory.create_base()
    creature_evolved = transform_factory.create_evolved()

    print(" base:")
    print(creature_base.describe())
    print(creature_base.attack())
    print(creature_base.transform())
    print(creature_base.attack())
    print(creature_base.revert())
    print(" evolved:")
    print(creature_evolved.describe())
    print(creature_evolved.attack())
    print(creature_evolved.transform())
    print(creature_evolved.attack())
    print(creature_evolved.revert())


def main() -> None:
    testing_creature_heal()
    testing_creature_transform()


if __name__ == "__main__":
    main()
