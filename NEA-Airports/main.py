import menu_system
import csv


def main():
    formatted_airport_data = {
        "UK Airports": {
            "LPL": "Liverpool John Lennon",
            "BOH": "Bournemouth International"
        },
        "Overseas Airports": None
    }

    aircraft_types = {
        "Medium narrow body": {
            "Running cost per seat per 100km": 8,
            "Maximun flight range": 2650,
            "Capacity": 180,
            "Minimum number of first class seats": 8
        },
        
        "Large narrow body": {
            "Running cost per seat per 100km": 7,
            "Maximun flight range": 5600,
            "Capacity": 220,
            "Minimum number of first class seats": 10
        },
        "Medium wide body": {
            "Running cost per seat per 100km": 5,
            "Maximun flight range": 4050,
            "Capacity": 406,
            "Minimum number of first class seats": 14
        }
    }

    airport_data = read_airports_data()
    formatted_airport_data["Overseas Airports"] = process_airports_data(airport_data)

    menu = menu_system.Menu(formatted_airport_data, aircraft_types)
    menu_handler(menu, formatted_airport_data)

def read_airports_data():
    with open("Airports.txt") as f:
        reader = csv.reader(f, delimiter=",")
        data = [
            row for row in reader
            if len(row)
        ]

    return data

def process_airports_data(data):
    formatted_airport_data = {
        
        airport_data[0]: {
            "Airport name": airport_data[1],
            "Distance from Liverpool John Lennon": airport_data[2],
            "Distance from Bournemouth Interational": airport_data[3]
        }
        for i, airport_data in enumerate(data)
    }

    return formatted_airport_data


def menu_handler(menu, airport_data):
    in_menu = True

    while in_menu:
        uk_airport_code = None
        overseas_airport_code = None
        aircraft_type = None
        num_of_first_class_seats = None
        distance = None
    
        while menu.option == None:
            menu.setup_menu()
            menu.get_menu_options()

            if menu.option == menu.commands[0]:
                uk_airport_code, overseas_airport_code = menu.enter_airport_details()
                uk_airport_details = airport_data["UK Airports"][uk_airport_code]
                overseas_airport_details = airport_data["Overseas Airports"][overseas_airport_code]

            elif menu.option == menu.commands[1]:
                aircraft_type, num_of_first_class_seats, num_of_stardard_class_seats = menu.enter_flight_details()
                
            elif menu.option == menu.commands[2]:
                menu.enter_price_plan(uk_airport_code, overseas_airport_code, aircraft_type, num_of_first_class_seats, num_of_stardard_class_seats)
                
            elif menu.option == menu.commands[3]:
                print("data cleared")
                
            elif menu.option == menu.commands[4]:
                in_menu = False
                
            else:
                print("Illegal input, please try again")

            menu.option = None

    menu.quit_menu()

            
if __name__ == "__main__":
    main()
