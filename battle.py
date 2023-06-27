from heroes import IronMan, CaptainAmerica, Thor, Hulk

class AvengersGame:
    """A class representing an Avengers game."""

    def __init__(self):
        """Initializes the default heroes."""
        self.heroes = [IronMan(), CaptainAmerica(), Thor(), Hulk()]

    def display_heroes(self):
        """Displays the heroes in the game."""
        print("Avengers Heroes:")
        for i, hero in enumerate(self.heroes, start=1):
            print(f"{i}. {hero.name}")

    def choose_hero(self, message):
        """Allows the user to choose a hero.

             Args:
                 message: A string to display to choose a hero.
             Returns:
                 The chosen hero or None if no valid choice was made.
             """
        while True:
            self.display_heroes()
            choice = input(message)

            if choice == "0":
                return None

            try:
                hero_index = int(choice) - 1
                return self.heroes[hero_index]
            except (IndexError, ValueError):
                print("This hero doesn't exist!\n")


if __name__ == "__main__":
    game = AvengersGame()
    game.play()
