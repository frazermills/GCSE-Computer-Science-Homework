# Author: Frazer Mills
# Date: 05/03/21
# program name: 'main.py'
# Python 3.9.2
# Description: This program is a GUI calculator that takes two numbers and performs an operation chosen by the user.

import pygame
import Menu_System

# ------------------------------------- Main Program Function ----------------------------------- #
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
    
    WIDTH = 400
    HEIGHT = 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    fps = 30
    result = 0
    text_colour = BLACK
    button_colour = WHITE
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Caculator - by Frazer Mills")
    clock = pygame.time.Clock()
    text_font = pygame.font.SysFont("Arial", 40)
    
    while True:
        nums, operator = menu_handler(screen, clock, WHITE, text_colour, text_font, result)
        result = operation_handler(nums, operator)
        pygame.display.update()
        clock.tick(fps)

# ----------------------------------------- Menu Handler ---------------------------------------- #
def menu_handler(screen, clock, button_colour, text_colour, text_font, result):
    """
    Dectects when a button is pressed.

    Parameters
    ----------
        screen: <class 'pygame.Surface'>
            The pygame surface where everything is rendered.           
        clock: <class 'Clock'>
            Maintains a constant frame rate.
        button_colour: tuple
            Colour of the buttons.
        text_colour: tuple
            Colour of text.
        text_font: <class 'pygame.font.Font'>
            Style and size of text.
        result: int, float
            Result from a calcualtion.

    Returns
    -------
        nums: list
            The 2 numbers used in the calculation.
        operator: str
            The operator in the calculation.
    """
    
    menu = Menu_System.Menu(screen, clock, button_colour, text_colour, text_font, result)
    operator = None
    nums = []

    menu.setup()
    
    while menu.option != "calc":
        menu.option = None
        menu.draw()
        menu.is_clicked()
        
        if menu.option == "1":
            print("button 1 clicked")
            nums.append(1)
            
        elif menu.option == "2":
            print("button 2 clicked")
            nums.append(2)

        elif menu.option == "3":
            print("button 3 clicked")
            nums.append(3)

        elif menu.option == "4":
            print("button 4 clicked")
            nums.append(4)

        elif menu.option == "5":
            print("button 5 clicked")
            nums.append(5)

        elif menu.option == "6":
            print("button 6 clicked")
            nums.append(6)

        elif menu.option == "7":
            print("button 7 clicked")
            nums.append(7)

        elif menu.option == "8":
            print("button 8 clicked")
            nums.append(8)

        elif menu.option == "9":
            print("button 9 clicked")
            nums.append(9)

        elif menu.option == "+":
            print("add button clicked")
            operator = "+"

        elif menu.option == "-":
            print("subtract button clicked")
            operator = "-"

        elif menu.option == "*":
            print("multiply button clicked")
            operator = "*"

        elif menu.option == "/":
            print("divide button clicked")
            operator = "/"

    return nums, operator

# --------------------------------------- Operation Handler ------------------------------------- #
def operation_handler(nums, operator):
    """
    Performs one of the following operations:
        * Add,
        * Subtract,
        * Multiply,
        * Divide.

    Parameters
    ----------
        nums: list
            A list of the 2 numbers.
        operator: str
            The selected calucation by user.

    Returns
    -------
        result: int, float
            Result of operation.
    """
    
    result = 0

    if operator == "+":
        result = sum(nums)
        
    elif operator == "-":
        result = nums[0] - nums[1]
        
    elif operator == "*":
        result = round(nums[0] * nums[1], 3)

    elif operator == "/":
        result = round(nums[0] / nums[1], 3)

    else:
        result = "illegal input"

    return result

# ------------------------------------------- Runs Main ----------------------------------------- #
if __name__ == "__main__":
    main()
