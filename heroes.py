class Heroes:
    """A class representing a hero."""

    def __init__(self, name: str, power: str, damage: int, phrase: str):
        """Initializes a new hero with the given name, power, damage and victory phrase."""

        self.name = name                # A string representing the hero name.
        self.power = power              # A string representing the hero power.
        self.damage = damage            # An integer representing the hero damage.
        self.victory_phrase = phrase    # A string representing the hero victory phrase.

    def display_info(self):
        """Displays information about the hero."""

        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Damage: {self.damage}")
        print(f"Victory Phrase: {self.victory_phrase}")

class IronMan(Heroes):
    """A class representing Iron Man, a subclass of Heroes."""

    def __init__(self):
        """Initializes a new Iron Man."""
        super().__init__("Iron Man", "Unibeam!", 50, "I see a armor around the world.")
        self.armor_mark = "Mark 42"

    def display_info(self):
        """Displays information about Iron Man."""
        super().display_info()
        print(f"Armor: {self.armor_mark}")

    def victory_info(self):
        """Displays information about Iron Man victory."""
        super().display_info()
        print(f"Iron Man: I see a armor around the world.")

class Hulk(Heroes):
    """A class representing Hulk, a subclass of Heroes."""

    def __init__(self):
        """Initializes a new Hulk."""
        super().__init__("Hulk", "Hulk SMASH!", 90, "HULK SMASH!")
        self.hulk_information = "If you calm him down, he will be fine."

    def display_info(self):
        """Displays information about Hulk."""
        super().display_info()
        print(f"Alert! {self.hulk_information}")

    def victory_info(self):
        """Displays information about Hulk victory."""
        super().display_info()
        print(f"HULK SMASH!")

class CaptainAmerica(Heroes):
    """A class representing Captain America, a subclass of Heroes."""

    def __init__(self):
        """Initializes a new Captain America."""
        super().__init__("Captain America", "Superhuman strength", 30, "I fight for peace!")
        self.soldier_characteristic = "Steve Rogers: Good soldiers follow orders."

    def display_info(self):
        """Displays information about Captain America."""
        super().display_info()
        print(f"Characteristic: {self.soldier_characteristic}")

    def victory_info(self):
        """Displays information about Captain America victory."""
        super().display_info()
        print(f"Captain America: I fight for peace!")

class Thor(Heroes):
    """A class representing Thor, a subclass of Heroes."""

    def __init__(self):
        """Initializes a new Thor."""
        super().__init__("Thor", "Lightning power", 90, "I am the god of THUNDER!")
        self.weapon = "Mjolnir"

    def display_info(self):
        """Displays information about Thor."""
        super().display_info()
        print(f"Weapon: {self.weapon}")

    def victory_info(self):
        """Displays information about Thor victory."""
        super().display_info()
        print(f"Thor: I am the god of THUNDER!")
