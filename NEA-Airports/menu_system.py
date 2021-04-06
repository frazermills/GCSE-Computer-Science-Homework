# Author: Frazer Mills
# Date: 06/04/21
# File name: 'menu_system.py'
# Program name: 'NEA - Airports'
# Python 3.9.2
# Description: This module contains the 'MenuSystem' class. An object of this class is instantiated in 'main.py'.
#              This object is used for the menu system. This object is managed by the 'menu_handler' function in 'main.py'.

# --------------------------------------------- MenuSystem Class ------------------------------------------- #
class MenuSystem:
    """
    A class to represent a menu. It also defines all of the menu system's options.

    Attributes
    ----------
        __commands: list
            Contains the menu's options.
        __choice: bool
            The user's menu choice.
        __option: bool
            The corresponding menu option to __choice
        __distance: int
            The distance (km) between the two airports.
        __airport_data: dict (3 dimensional dictionary)
            Contains all of the data from the Airports.txt file.
        __valid_codes: dict (2 dimensional dictionary)
            Used to validate the codes from Airport.txt file.
        __aircraft_types: dict (2 dimensional dictionary)
            Contains all data on the Aircraft models and their specifications.
        __developer: str
            The developer of the program.
        __company: str
            The name of the company the program is licensed to.

    Special Methods
    ---------------
        __init__(): Method
            Initialises all of the attributes of the class.
        __del__(): Method
            Deconstructs the class.

    Methods used for Encapsulation
    ------------------------------
        AirportData(): Getter Method
            Gets self.__airport_data.
        Choice(): Getter Method
            Gets self.__choice.
        Option(): Getter Method
            Gets self.__option.
        Commands(): Getter Method
            Gets self.__commands.
        
        Choice(): Getter Method
            Sets self.__choice to no other value than 'None'. Used to reset the attribute.
            A 'ValueError' will be raised if the attribute is set to a value other than 'None'.
        Option(): Getter Method
            Sets self.__option to no other value than 'None'. Used to reset the attribute.
            A 'ValueError' will be raised if the attribute is set to a value other than 'None'.
            
    Static Methods
    --------------
        formmatting():
            Used to format the menu. Can format with a horizontal rule,
            or can 'clear the screen' by printing 60 '\n'.

    Methods
    -------
        setup_menu():
            Prints menu options to display. Takes input from user.
        get_menu_options():
            Assigns a menu option depending on the user's choice.
        enter_airport_details():
            Prompts the user to input a three letter airport code for the UK and Overseas airports.
            Prints which overseas airport the user has selected.
        enter_flight_details():
            Prompts the user to input the aircraft type and details.
            Prompts the user to input the number of first class seats.
            Calculates the number of standard seats.
        enter_price_plan():
            Validates the following things:
                1. The user has inputted suitable airport codes.
                2. The user has inputted a suitable aircraft type.
                3. The user has inputted a suitable number of first class seats.
            Prompts user to input the cost per first class and standard class seat.
            Claculates the cost per seat, flight cost, flight income, flight profit.
            Outputs the flight's profit to the display.
        quit_menu():
            Outputs a goodbye message to the user.
    """

# ------------------------------------------ Initialises Attributes ---------------------------------------- #
    def __init__(self, airport_data, aircraft_types):
        """
        Constructs all of the necessary attributes for the Menu object.

        Parameters
        ----------
            airport_data: dict (3 dimensional dictionary)
                Contains all of the data from the Airports.txt file.
            aircraft_types: dict (2 dimensional dictionary)
                Contains all data on the Aircraft models and their specifications.

        Returns
        -------
            None.
        """
        
        self.__commands = [
            "1 - Enter airport details",
            "2 - Enter flight details",
            "3 - Enter price plan",
            "4 - Clear data", "9 - Quit"
        ]
        self.__choice = None
        self.__option = None
        self.__distance = None
        self.__chosen_aircraft = None
        self.__airport_data = airport_data
        self.__valid_codes = {
            "UK Airports": [*self.__airport_data["UK Airports"]],
            "Overseas Airports": [*self.__airport_data["Overseas Airports"]]
        }        
        self.__aircraft_types = aircraft_types
        self.__developer = "Frazer Mills"
        self.__company = "Airport Manager LLC"

# -------------------------------------------- Deconstructs Class ------------------------------------------ #
    def __del__(self):
        """
        Decontructs the menu object.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        
        print("All data has been cleared")

# ---------------------------------------- Setter and Getter Methods --------------------------------------- #
    @property
    def AirportData(self):
        return self.__airport_data

    @property
    def Choice(self):
        return self.__choice

    @Choice.setter
    def Choice(self, value):
        if value == None:
            self.__choice = value
        else:
            raise Exception(f"{value} is an ivalid reset value, '__choice' can only be reset to 'None'")
    
    @property
    def Option(self):
        return self.__option

    @Option.setter
    def Option(self, value):
        if value == None:
            self.__option = value
        else:
            raise Exception(f"{value} is an ivalid reset value, '__option' can only be reset to 'None'")

    @property
    def Commands(self):
        return self.__commands

# --------------------------------------------- Formats Display -------------------------------------------- #
    @staticmethod
    def formatting(mode):
        """
        Adds visual formatting to the menu system.

        Parameters
        ----------
            mode: str
                Used to choose between the different modes of the methods.

        Returns
        -------
            None
        """
        
        if mode == "clear display":
            for i in range(60):
                print("\n")

        elif mode == "print horizontal rule":
            print("=" * 80)

        else:
            raise Exception(f"'{mode}' is an unsported mode of the static method 'formatting'")

# ------------------------------------------ Displays Menu Options ----------------------------------------- #
    def setup_menu(self):
        """
        Prints menu options to display. Takes input from user.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        
        for index, command in enumerate(self.__commands):
            print(command)

        while self.__choice == None:
            try:
                self.__choice = int(input("menu choice >>> "))

            except ValueError:
                print("That was an illegal value input, please try again.")

# -------------------------------------------- Gets Menu Options ------------------------------------------- #
    def get_menu_options(self):
        """
        Assigns a menu option depending on the user's choice.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        
        if self.__choice == 1:
            self.__option = self.__commands[0]

        elif self.__choice == 2:
            self.__option = self.__commands[1]

        elif self.__choice == 3:
            self.__option = self.__commands[2]

        elif self.__choice == 4:
            self.__option = self.__commands[3]

        elif self.__choice == 9:
            self.__option = self.__commands[4]

# --------------------------------------- Prompts for Airport Details -------------------------------------- #
    def enter_airport_details(self):
        """
        Prompts user to enter the airport data.

        Parameters
        ----------
            None

        Returns
        -------
            three_letter_uk_airport_code: str
                Used for validation of Airports from Airports.txt.
            three_letter_overseas_airport_code: str
                Used for validation of Airports from Airports.txt.
        """
        
        three_letter_uk_airport_code = str(input("Input three letter UK Airport code >>> "))
        while three_letter_uk_airport_code not in self.__valid_codes["UK Airports"]:
            print("Invalid UK Airport code, please try again")
            three_letter_uk_airport_code = str(input("Input three letter UK Airport code >>> "))

        three_letter_overseas_airport_code = str(input("Input three letter Overseas Airport code >>> "))
        while three_letter_overseas_airport_code not in self.__valid_codes["Overseas Airports"]:
            print("Invalid Overseas Airport code, please try again")
            three_letter_overseas_airport_code = str(input("Input three letter Overseas Airport code >>> "))

        chosen_overseas_airport = self.__airport_data["Overseas Airports"][three_letter_overseas_airport_code]["Airport name"]
        print(f"You have selected to fly to {chosen_overseas_airport} Airport")

        if three_letter_uk_airport_code == "LPL":
            self.__distance = self.__airport_data["Overseas Airports"][three_letter_overseas_airport_code]["Distance from Liverpool John Lennon"]
        elif three_letter_uk_airport_code == "BOH":
            self.__distance = self.__airport_data["Overseas Airports"][three_letter_overseas_airport_code]["Distance from Bournemouth Interational"]

        return three_letter_uk_airport_code, three_letter_overseas_airport_code

# ---------------------------------------- Prompts for Flight Details -------------------------------------- #
    def enter_flight_details(self):
        """
        Prompts user for inputs. Calculates number of seats on.

        Parameters
        ----------
            None

        Returns
        -------
            num_of_first_class_seats: int
                The number of seats on the plan that are first class.
            num_of_stardard_class_seats: int
                The number of seats on the plan that are standard class.
        """
        
        num_of_aircrafts = len(self.__aircraft_types)
        chosen_aircraft = None
        num_of_first_class_seats = None
        max_num_of_first_class_seats = None
        
        print("Type | Running cost per seat per 100 km | Maximum flight range (km) | Capacity if all seats are standard-class | Minimum number of first-class seats (if there are any)")
        for i, aircraft in enumerate(self.__aircraft_types):
            running_cost = self.__aircraft_types[aircraft]["Running cost per seat per 100km"]
            max_range = self.__aircraft_types[aircraft]["Maximun flight range"]
            capacity = self.__aircraft_types[aircraft]["Capacity"]
            min_first_class_seats = self.__aircraft_types[aircraft]["Minimum number of first class seats"]
            print(f"{aircraft} | {running_cost} | {max_range} | {capacity} | {min_first_class_seats} | option number: {i + 1}")        

        chosen_aircraft_num = str(input(f"Input your chosen aircraft type option (1 to {num_of_aircrafts}): "))

        while self.__chosen_aircraft == None:
            if chosen_aircraft_num == "1":
                self.__chosen_aircraft = "Medium narrow body"
            elif chosen_aircraft_num == "2":
                self.__chosen_aircraft = "Large narrow body"
            elif chosen_aircraft_num == "3":
                self.__chosen_aircraft = "Medium wide body"
            else:
                chosen_aircraft_num = str(input(f"That is an illegal input, please try again. Input your chosen aircraft type option (1 to {num_of_aircrafts}): "))
        print("Input accepted")

        max_num_of_first_class_seats = self.__aircraft_types[self.__chosen_aircraft]["Capacity"] // 2
        
        while num_of_first_class_seats == None:
            num_of_first_class_seats = int(input("Input the number of first class seats: "))

            if num_of_first_class_seats:
                if num_of_first_class_seats < self.__aircraft_types[self.__chosen_aircraft]["Minimum number of first class seats"]:
                    print(f"The minimum number of first class seats for this aircraft is {self.aircraft_types[self.__chosen_aircraft]['Minimum number of first class seats']},", end=" ")
                    print(f"your input of {num_of_first_class_seats} was too low. Please try again.")
                    num_of_first_class_seats = None

            elif num_of_first_class_seats > max_num_of_first_class_seats:
                print(f"The maximum capacity for first class seats is {max_num_of_first_class_seats}, your input of {num_of_first_class_seats} was too big. Please try again.")
                num_of_first_class_seats = None

            elif num_of_first_class_seats == 0:
                if self.__aircraft_types[chosen_aircraft]["Minimum number of first class seats"] == 0:
                    continue
                else:
                    print(f"The minimum number of first class seats for this aircraft is {self.__aircraft_types[chosen_aircraft]['Minimum number of first class seats']}," , end=" ")
                    print(f"your input of {num_of_first_class_seats} was too low. Please try again.")
                    num_of_first_class_seats = None

        print("Inputs accepted")

        num_of_stardard_class_seats = self.__aircraft_types[self.__chosen_aircraft]["Capacity"] - (num_of_first_class_seats * 2)

        return num_of_first_class_seats, num_of_stardard_class_seats

# -------------------------------------- Prompts for Price Plan Details ------------------------------------ #
    def enter_price_plan(self, uk_airport_code, overseas_airport_code, num_of_first_class_seats, num_of_stardard_class_seats):
        """
        Calculates the flight's profit.

        Parameters
        ----------
            uk_airport_code: str
                Three letter code that define which airport the user is travelling from.
            overseas_airport_code: str
                Three letter code that define which airport the user is travelling to.
            

        Returns
        -------
            None
        """
        
        try:
            if uk_airport_code in self.__valid_codes["UK Airports"] and overseas_airport_code in self.__valid_codes["Overseas Airports"]:

                if self.__chosen_aircraft in self.__aircraft_types:
                    
                    if num_of_first_class_seats:
                        
                        if self.__aircraft_types[self.__chosen_aircraft]["Maximun flight range"] >= int(self.__distance):
                            cost_per_first_class_seat = int(input("Input cost per first class seat: "))
                            flight_cost_per_standard_seat = int(input("Input cost per standard seat: "))
                            
                            flight_cost_per_seat = (self.__aircraft_types[self.__chosen_aircraft]["Running cost per seat per 100km"] * int(self.__distance)) / 100
                            flight_cost = flight_cost_per_seat * (num_of_first_class_seats + num_of_stardard_class_seats)
                            flight_income = (num_of_first_class_seats * cost_per_first_class_seat) + (num_of_stardard_class_seats * flight_cost_per_standard_seat) 
                            flight_profit = round(flight_income - flight_cost, 2)

                            print(f"cost per seat: {flight_cost_per_seat} | flight_cost: {flight_cost} | flight income: {flight_income} | flight profit: {flight_profit}")

                        else:
                            print("The maximum flight range of the chosen aircraft is not big enough to cover the distance required. Please try again.")
                        
                    else:
                        print("Please input the Number of First Class Seats there will be first")

                else:
                    print("Please input the Aircraft Type you will be using.")

            else:
                print("Please input the UK and Overseas Airports you will be using.")

        except UnboundLocalError:
            print("You need to do 'Enter airport details' and 'Enter flight details' first. Please try again after doing so.")

# ------------------------------------------------ Quits Menu ---------------------------------------------- #
    def quit_menu(self):
        """
        Outputs a goodbye message to the display.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        
        print(f"Thank you for using this program.\nThis program was created by {self.__developer} from {self.__company}")
