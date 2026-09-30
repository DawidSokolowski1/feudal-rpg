"""Character creation: asks for the player's name, age and birthday.

Note: the Intro class is currently not used by the game itself.
"""


class Intro():
    """Asks the player for their details when an Intro object is created."""

    def __init__(self):
        """Run the three questions in order and store the answers."""
        self.name = self.get_name()
        self.age = self.get_age()
        self.zodiac = self.get_zodiac()

    def get_name(self):
        """Ask for the player's name and return it.

        An empty input asks whether the player wants to stay anonymous:
        1 gives the name "Unknown", anything else asks for the name again.
        The while loop repeats as long as name is still empty.
        """
        name = ""
        while not name:
            name = input('Enter your name unknown ')
            if not name:
                print('\nAre u sure u want to stay anonymous?'
                      + "\n Press 1 if yes "
                      + "\n Press any other number if no")
                choice = input()
                try:
                    choice = int(choice)
                except ValueError:
                    print('\nOnly numbers are accepted!')
                if choice == 1:
                    name = "Unknown"
                else:
                    name = ""
        return name

    def get_age(self):
        """Ask for the player's age (13-90) and return it.

        int() raises a ValueError for anything that isn't a number; except
        catches it and the loop asks again. Ages outside 13-90 are refused.
        """
        while True:
            try:
                age = int(input("\nEnter your age, the proper fighting "
                                "abilities can be gained first from age "
                                "of 13 \n "))
                if age < 13:
                    print("\nYou will not make it kid")
                    continue
                elif age > 90:
                    print("\nIt's not a game about vampires")
                else:
                    return age
            except ValueError:
                print("\nYou need to enter a number!")

    def get_zodiac(self):
        """Ask for the birth month and day and return the zodiac sign.

        First asks for the month, then the day (checked against the number
        of days in the month). Each zodiac sign is stored with its start and
        end date as (month, day) tuples. Python compares tuples element by
        element, so (month, day) >= start checks the month first and then
        the day.
        """
        while True:
            try:
                month = int(input("\n Enter the month of your birth "
                                  "with a number: "))
                if month > 12:
                    print("Only numbers from 1 until 12 are accepted!")
                    continue
                else:
                    break
            except ValueError:
                print("\nYou need to enter a number!")
        while True:
            # Number of days in each month, January to December
            month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            # month_check checks the month positon in the list
            month_check = month - 1
            try:
                day = int(input("\n Enter the day of your birth "
                                "with a number: "))
                if day > month_days[month]:
                    print("This month has only " + str(month_days[month])
                          + " days!")
                    continue
                else:
                    break
            except ValueError:
                print("\nYou need to enter a number!")
        # (sign, (start month, start day), (end month, end day))
        zodiacs = [
            ("Aries", (3, 21), (4, 19)),
            ("Taurus", (4, 20), (5, 20)),
            ("Gemini", (5, 21), (6, 20)),
            ("Cancer", (6, 21), (7, 22)),
            ("Leo", (7, 23), (8, 22)),
            ("Virgo", (8, 23), (9, 22)),
            ("Libra", (9, 23), (10, 22)),
            ("Scorpio", (10, 23), (11, 21)),
            ("Sagittarius", (11, 22), (12, 21)),
            ("Capricorn", (12, 22), (1, 19)),
            ("Aquarius", (1, 20), (2, 18)),
            ("Pisces", (2, 19), (3, 20)),
        ]
        for sign, start, end in zodiacs:
            if (month, day) >= start and (month, day) <= end:
                print(sign)
                return sign


# intro=Intro()
# print("Hello " + intro.name + " you are " + str(intro.age)
#       + " years old and u got blessed by the " + intro.zodiac
#       + "stars." )
