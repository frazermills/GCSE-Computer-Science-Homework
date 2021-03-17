# Airports NEA example

DEBUG = True # Flag to enable/disable tracing

import csv # Import the CSV (comma separated values) module

# -----------------------------------------------
def show_menu():
  print_horizontal_rule()
  print("MENU:")
  print("1 - Enter airport details")
  print("2 - Enter flight details")
  print("3 - Enter price plan")
  print("4 - Clear data")
  print("9 - Quit")
# -----------------------------------------------
def read_airports_data():
  data = []

  # open a file
  with open("Airports.txt") as f:
    # get a CSV reader object
    reader = csv.reader(f, delimiter=",")
    # iterate over each row
    for row in reader:
      if len(row):
        print(row)
        data.append(row)
  return data  
# -----------------------------------------------
def main():
  data = read_airports_data()
  if DEBUG: print(data)

  show_menu()

  # get first choice
  choice = int(input("Choose a menu option "))

  while choice != 9:
    # do the chosen item
    if choice == 1:
      enter_airport_details()
    elif choice == 2:
      enter_flight_details()
    elif choice == 3:
      enter_price_plan()
    elif choice == 4:
      clear_data()  
    else:
      print("Illegal choice")

    show_menu()
    # get next choice
    choice = int(input("Choose a menu option "))

# -----------------------------------------------
def clear_display():
  print("\n" * 60)
# -----------------------------------------------
def print_horizontal_rule():
  print("=" * 30)
# -----------------------------------------------
def enter_airport_details():
  pass
# -----------------------------------------------
def enter_flight_details():
  pass  
# -----------------------------------------------
def enter_price_plan():
  pass    
# -----------------------------------------------
def clear_data():
  pass    
# -----------------------------------------------

main()
