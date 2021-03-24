
class Menu:
  def __init__(self):
    self.commands = ["1 - Enter airport details", "2 - Enter flight details", "3 - Enter price plan", "4 - Clear data", "9 - Quit"]
    self.choice = None
    self.option = None

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
  
  def menu_options(self):
    if self.choice == 1:
      self.option = self.commands[0]

    elif self.choice == 2:
      self.option = self.commands[1]

    elif self.choice == 3:
      self.option = self.commands[2]

    elif self.choice == 4:
      self.option = self.commands[3]
  
  def update_menu(self):
    print(self.option)
    if self.option == self.commands[0]:
      print("1 - Enter airport details")
    elif self.option == self.commands[1]:
      print("2 - Enter flight details")
    elif self.option == self.commands[2]:
      print("3 - Enter price plan")
    elif self.option == self.commands[3]:
      print("4 - Clear data")
    elif self.option == self.commands[4]:
      print("9 - Quit")
