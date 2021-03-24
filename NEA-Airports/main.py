import menu_system
import csv


def main():
    airport_data = read_airports_data()
    print(airport_data)
    menu = menu_system.Menu()
    menu_handler(menu)


def read_airports_data():
    data = []

    with open("Airports.txt") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if len(row):
                print(row)
                data.append(row)
    return data


def menu_handler(menu):
    in_menu = True

    while in_menu:
      while menu.option == None:
          menu.setup_menu()
          if menu.choice == 1:
              menu.menu_options()
          elif menu.choice == 2:
              menu.menu_options()
          elif menu.choice == 3:
              menu.menu_options()
          elif menu.choice == 4:
              menu.menu_options()
          elif menu.choice == 9:
              menu.menu_options()
          
          menu.update_menu()
            
if __name__ == "__main__":
    main()
