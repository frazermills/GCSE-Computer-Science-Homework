class Menu:
    def __init__(self, airport_data, aircraft_types):
        self.commands = ["1 - Enter airport details", "2 - Enter flight details", "3 - Enter price plan", "4 - Clear data", "9 - Quit"]
        self.choice = None
        self.option = None
        self.airport_data = airport_data
        self.valid_codes = {
            "UK Airports": [*self.airport_data["UK Airports"]],
            "Overseas Airports": [*self.airport_data["Overseas Airports"]]
        }
        self.aircraft_types = aircraft_types
        self.developer = "Frazer Mills"
        self.company = "Airport Manager LLC"

    def setup_menu(self):
        for index, command in enumerate(self.commands):
            print(command)
        self.choice = int(input("menu choice >>> "))

    def formatting(self, mode):
        if mode == "clear_display":
            for i in range(60):
                print("\n")

        elif mode == "print_horizontal_rule":
            print("=" * 60)

        elif mode == "clear_data":
            print("data cleared")

    def get_menu_options(self):
        if self.choice == 1:
            self.option = self.commands[0]

        elif self.choice == 2:
            self.option = self.commands[1]

        elif self.choice == 3:
            self.option = self.commands[2]

        elif self.choice == 4:
            self.option = self.commands[3]

        elif self.choice == 9:
            self.option = self.commands[4]

    def update_menu(self):
        print(self.option)
        if self.option == self.commands[0]:
            self.enter_airport_details()
        elif self.option == self.commands[1]:
            print("2 - Enter flight details")
        elif self.option == self.commands[2]:
            print("3 - Enter price plan")
        elif self.option == self.commands[3]:
            print("4 - Clear data")
        elif self.option == self.commands[4]:
            print("9 - Quit")

    def enter_airport_details(self):
        three_letter_uk_airport_code = str(input("Input three letter UK Airport code >>> "))
        while three_letter_uk_airport_code not in self.valid_codes["UK Airports"]:
            print("Invalid UK Airport code, please try again")
            three_letter_uk_airport_code = str(input("Input three letter UK Airport code >>> "))

        three_letter_overseas_airport_code = str(input("Input three letter Overseas Airport code >>> "))
        while three_letter_overseas_airport_code not in self.valid_codes["Overseas Airports"]:
            print("Invalid Overseas Airport code, please try again")
            three_letter_overseas_airport_code = str(input("Input three letter Overseas Airport code >>> "))

        chosen_airport = self.airport_data["Overseas Airports"][three_letter_overseas_airport_code]["Airport name"]
        print(f"You have selected to fly to {chosen_airport} Airport")

        return three_letter_uk_airport_code, three_letter_overseas_airport_code

    def enter_flight_details(self):
        pass

    def enter_price_plan(self):
        pass

    def clear_data(self):
        pass

    def quit_menu(self):
        print(f"Thank you for using this program.\nThis program was created by {self.developer} from {self.company}")
        quit()

