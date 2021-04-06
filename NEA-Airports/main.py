import menu_system
import csv

def main():
    """
    It initialises all the variables used in the program and runs the main loop.

    Parameters
    ----------
        None
        
    Returns
    -------
        None
    """
    
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

    while True:
        menu = menu_system.MenuSystem(formatted_airport_data, aircraft_types)
        menu_handler(menu, formatted_airport_data)
        input("Press enter to continue")
        menu_system.MenuSystem.formatting("print horizontal rule")
        menu_system.MenuSystem.formatting("clear display")

def read_airports_data():
    """
    Reads data from Airport.txt file and puts it into a 2 dimensional array.

    Parameters
    ----------
        None
        
    Returns
    -------
        data: list
            Contains data from Airport.txt.
    """
    
    with open("Airports.txt") as f:
        reader = csv.reader(f, delimiter=",")
        data = [
            row for row in reader
            if len(row)
        ]

    return data

def process_airports_data(data):
    """
    Formats data into a 3 dimensional dictionary.

    Parameters
    ----------
        data: list
            Contains data from Airport.txt.
        
    Returns
    -------
        formatted_airport_data: dict (3 dimensional dictionary)
            Contains formatted data from Airport.txt.
    """
    
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
    """
    Dectects when the user inputs a command.
    
    Parameters
    ----------
        airport_data: dict (3 dimensional dictionary)
            Contains formatted data from Airport.txt. 
    Returns
    -------
        None
    """
    
    in_menu = True

    while in_menu:
        uk_airport_code = None
        overseas_airport_code = None
        aircraft_type = None
        num_of_first_class_seats = None
        
        while menu.Option == None:
            menu_system.MenuSystem.formatting("print horizontal rule")
            menu.setup_menu()
            menu.get_menu_options()

            if menu.Option == menu.Commands[0]:
                uk_airport_code, overseas_airport_code = menu.enter_airport_details()
                uk_airport_details = airport_data["UK Airports"][uk_airport_code]
                overseas_airport_details = airport_data["Overseas Airports"][overseas_airport_code]
                menu_system.MenuSystem.formatting("print horizontal rule")

            elif menu.Option == menu.Commands[1]:
                aircraft_type, num_of_first_class_seats, num_of_stardard_class_seats = menu.enter_flight_details()
                menu_system.MenuSystem.formatting("print horizontal rule")
                
            elif menu.Option == menu.Commands[2]:
                menu.enter_price_plan(uk_airport_code, overseas_airport_code, aircraft_type, num_of_first_class_seats, num_of_stardard_class_seats)
                menu_system.MenuSystem.formatting("print horizontal rule")
                
            elif menu.Option == menu.Commands[3]:
                clear_data(menu)
                in_menu = False
                break

            elif menu.Option == menu.Commands[4]:
                quit_program(menu)
                
            else:
                print("Illegal input, please try again")

            menu.Option = None
            menu.Choice = None
            

def clear_data(menu):
    """
    Clears data by resetting the program.

    Parameters
    ----------
        None
        
    Returns
    -------
        None
    """
    
    del menu

def quit_program(menu):
    """
    Quits the program and clears all data.

    Parameters
    ----------
        None
        
    Returns
    -------
        None
    """
    
    menu.quit_menu()
    del menu
    quit()


if __name__ == "__main__":
    main()
