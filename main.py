from heroes import IronMan, CaptainAmerica, Thor, Hulk
from battle import AvengersGame

def main():
    """Runs the Avengers game."""
    game = AvengersGame()

    print("Choose your favorite hero for the battle.\n")

    hero1 = game.choose_hero("Choose Avenger 1 : ")

    hero2 = game.choose_hero("Choose Avenger 2 : ")

    print("\n---------------------- The Battle has begun! ----------------------")

    print(f"{hero1.name} vs. {hero2.name}\n")

    print(f"{hero1.name}:")
    hero1.display_info()
    print()

    print(f"{hero2.name}:")
    hero2.display_info()
    print()

    if hero1.damage > hero2.damage:
        print(f"{hero1.name} wins the battle with {hero1.damage} damage vs {hero2.damage} from {hero2.name}!")
        print(f"{hero1.victory_phrase}")
    elif hero1.damage < hero2.damage:
        print(f"{hero2.name} wins the battle with {hero2.damage} damage vs {hero1.damage} from {hero1.name}!")
        print(f"{hero2.victory_phrase}")
    else:
        print("It's a tie! The battle ends in a draw.")


if __name__ == "__main__":
    main()
