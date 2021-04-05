class Menu:
    def __init__(self, airport_data, aircraft_types):
        self.commands = ["1 - Enter airport details", "2 - Enter flight details", "3 - Enter price plan", "4 - Clear data", "9 - Quit"]
        self.choice = None
        self.option = None
        self.distance = None
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

        chosen_overseas_airport = self.airport_data["Overseas Airports"][three_letter_overseas_airport_code]["Airport name"]
        print(f"You have selected to fly to {chosen_overseas_airport} Airport")

        if three_letter_uk_airport_code == "LPL":
            self.distance = self.airport_data["Overseas Airports"][three_letter_overseas_airport_code]["Distance from Liverpool John Lennon"]
        elif three_letter_uk_airport_code == "BOH":
            self.distance = self.airport_data["Overseas Airports"][three_letter_overseas_airport_code]["Distance from Bournemouth Interational"]

        return three_letter_uk_airport_code, three_letter_overseas_airport_code

    def enter_flight_details(self):
        num_of_aircrafts = len(self.aircraft_types)
        chosen_aircraft = None
        num_of_first_class_seats = None
        max_num_of_first_class_seats = None
        
        print("Type | Running cost per seat per 100 km | Maximum flight range (km) | Capacity if all seats are standard-class | Minimum number of first-class seats (if there are any)")
        for i, aircraft in enumerate(self.aircraft_types):
            running_cost = self.aircraft_types[aircraft]["Running cost per seat per 100km"]
            max_range = self.aircraft_types[aircraft]["Maximun flight range"]
            capacity = self.aircraft_types[aircraft]["Capacity"]
            min_first_class_seats = self.aircraft_types[aircraft]["Minimum number of first class seats"]
            print(f"{aircraft} | {running_cost} | {max_range} | {capacity} | {min_first_class_seats} | option number: {i + 1}")        

        chosen_aircraft_num = str(input(f"Input your chosen aircraft type option (1 to {num_of_aircrafts}): "))

        while chosen_aircraft == None:
            if chosen_aircraft_num == "1":
                chosen_aircraft = "Medium narrow body"
            elif chosen_aircraft_num == "2":
                chosen_aircraft = "Large narrow body"
            elif chosen_aircraft_num == "3":
                chosen_aircraft = "Medium wide body"
            else:
                chosen_aircraft_num = str(input(f"That is an illegal input, please try again. Input your chosen aircraft type option (1 to {num_of_aircrafts}): "))
        print("Input accepted")

        max_num_of_first_class_seats = self.aircraft_types[chosen_aircraft]["Capacity"] // 2
        
        while num_of_first_class_seats == None:
            num_of_first_class_seats = int(input("Input the number of first class seats: "))

            if num_of_first_class_seats:
                if num_of_first_class_seats < self.aircraft_types[chosen_aircraft]["Minimum number of first class seats"]:
                    print(f"The minimum number of first class seats for this aircraft is {self.aircraft_types[chosen_aircraft]['Minimum number of first class seats']}, your input of {num_of_first_class_seats} was too low. Please try again.")
                    num_of_first_class_seats = None

            elif num_of_first_class_seats > max_num_of_first_class_seats:
                print(f"The maximum capacity for first class seats is {max_num_of_first_class_seats}, your input of {num_of_first_class_seats} was too big. Please try again.")
                num_of_first_class_seats = None

            elif num_of_first_class_seats == 0:
                if self.aircraft_types[chosen_aircraft]["Minimum number of first class seats"] == 0:
                    continue
                else:
                    print(f"The minimum number of first class seats for this aircraft is {self.aircraft_types[chosen_aircraft]['Minimum number of first class seats']}, your input of {num_of_first_class_seats} was too low. Please try again.")
                    num_of_first_class_seats = None

        print("Inputs accepted")

        num_of_stardard_class_seats = self.aircraft_types[chosen_aircraft]["Capacity"] - (num_of_first_class_seats * 2)

        print(num_of_stardard_class_seats)

        return chosen_aircraft, num_of_first_class_seats, num_of_stardard_class_seats
        
    def enter_price_plan(self, uk_airport_code, overseas_airport_code, aircraft_type, num_of_first_class_seats, num_of_stardard_class_seats):
        if uk_airport_code in self.valid_codes["UK Airports"] and overseas_airport_code in self.valid_codes["Overseas Airports"]:

            if aircraft_type in self.aircraft_types:
                
                if num_of_first_class_seats:
                    
                    if self.aircraft_types[aircraft_type]["Maximun flight range"] >= int(self.distance):
                        cost_per_first_class_seat = int(input("Input cost per first class seat: "))
                        flight_cost_per_standard_seat = int(input("Input cost per standard seat: "))
                        
                        flight_cost_per_seat = (self.aircraft_types[aircraft_type]["Running cost per seat per 100km"] * int(self.distance)) / 100
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

    def clear_data(self):
        pass

    def quit_menu(self):
        print(f"Thank you for using this program.\nThis program was created by {self.developer} from {self.company}")
        quit()

