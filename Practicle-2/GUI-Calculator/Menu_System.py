# Author: Frazer Mills
# Date: 05/03/21
# program name: 'Menu_System.py'
# Python 3.9.2
# Description: This module contains the Menu class, which handles the buttons and text rendering and processing.

import pygame

# ------------------------------------------- Menu Class ----------------------------------------- #
class Menu:
    """
    A class to represent a menu.

    Attributes
    ----------
        screen: <class 'pygame.Surface'>
            The pygame surface where everything is rendered.           
        clock: <class 'Clock'>
            Maintains a constant frame rate.
        button_colour: tuple
            Colour of the buttons.
        text_colour: tuple
            Colour of text.
        font: <class 'pygame.font.Font'>
            Style and size of text.
        result: int, float
            Result from a calcualtion.

    Methods
    -------
        setup():
            Initilises all of the buttons' attributes.
        draw():
            Displays all of the buttons, with their text, to the screen.
        draw_text(text: <string>, x: <int>, y: <int>):
            draws the text string so that the centre is at the x and y locations.
        is_clicked():
            Checks if the user clicks on a button.
    """

# ------------------------------------- Initialises Attributes ----------------------------------- #
    def __init__(self, screen, clock, button_colour, text_colour, font, result):
        """
        Constructs all of the necessary attributes for the Menu object.

        Parameters
        ----------
            screen: <class 'pygame.Surface'>
                The pygame surface where everything is rendered.           
            clock: <class 'Clock'>
                Maintains a constant frame rate.
            colour: tuple
                Colour of the buttons.
            text_colour: tuple
                Colour of text.
            font: <class 'pygame.font.Font'>
                Style and size of text.
            result: int, float
                Result from a calcualtion.
            click: bool
                Keeps track of whether the mouse is clicked or not.
            button_size: int
                Defines the size of the buttons.
            option: str, optional
                Used to store the user's options.
                Can take on any value from button_command.
            button_command: list
                Stores all possible button commands
        """
        
        self.screen = screen
        self.clock = clock
        self.colour = button_colour
        self.text_colour = text_colour
        self.font = font
        self.result = result
        self.click = False
        self.button_size = 90
        self.option = None
        self.button_command = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "calc"]
# --------------------------------------- Sets up Calculator ------------------------------------- #
    def setup(self):
        """
        Sets each buttons' x,y positions.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        
        self.button_1_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 150, (self.screen.get_height() // 2) - 100)
        self.button_1 = pygame.Rect(self.button_1_xy[0], self.button_1_xy[1], self.button_size, self.button_size)

        self.button_2_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 50, (self.screen.get_height() // 2) - 100)
        self.button_2 = pygame.Rect(self.button_2_xy[0], self.button_2_xy[1], self.button_size, self.button_size)

        self.button_3_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 50, (self.screen.get_height() // 2) - 100)
        self.button_3 = pygame.Rect(self.button_3_xy[0], self.button_3_xy[1], self.button_size, self.button_size)

        self.button_4_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 150, (self.screen.get_height() // 2))
        self.button_4 = pygame.Rect(self.button_4_xy[0], self.button_4_xy[1], self.button_size, self.button_size)

        self.button_5_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 50, (self.screen.get_height() // 2))
        self.button_5 = pygame.Rect(self.button_5_xy[0], self.button_5_xy[1], self.button_size, self.button_size)

        self.button_6_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 50, (self.screen.get_height() // 2))
        self.button_6 = pygame.Rect(self.button_6_xy[0], self.button_6_xy[1], self.button_size, self.button_size)

        self.button_7_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 150, (self.screen.get_height() // 2) + 100)
        self.button_7 = pygame.Rect(self.button_7_xy[0], self.button_7_xy[1], self.button_size, self.button_size)

        self.button_8_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 50, (self.screen.get_height() // 2) + 100)
        self.button_8 = pygame.Rect(self.button_8_xy[0], self.button_8_xy[1], self.button_size, self.button_size)

        self.button_9_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 50, (self.screen.get_height() // 2) + 100)
        self.button_9 = pygame.Rect(self.button_9_xy[0], self.button_9_xy[1], self.button_size, self.button_size)

        self.button_add_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 150, (self.screen.get_height() // 2) - 100)
        self.button_add = pygame.Rect(self.button_add_xy[0], self.button_add_xy[1], self.button_size, self.button_size)

        self.button_subtract_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 150, (self.screen.get_height() // 2))
        self.button_subtract = pygame.Rect(self.button_subtract_xy[0], self.button_subtract_xy[1], self.button_size, self.button_size)

        self.button_multiply_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 150, (self.screen.get_height() // 2) + 100)
        self.button_multiply = pygame.Rect(self.button_multiply_xy[0], self.button_multiply_xy[1], self.button_size, self.button_size)

        self.button_divide_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 150, (self.screen.get_height() // 2) + 200)
        self.button_divide = pygame.Rect(self.button_divide_xy[0], self.button_divide_xy[1], self.button_size, self.button_size)

        self.button_calc_xy  = ((self.screen.get_width() // 2) - (self.button_size // 2) + 50, (self.screen.get_height() // 2) + 200)
        self.button_calc = pygame.Rect(self.button_calc_xy[0], self.button_calc_xy[1], self.button_size, self.button_size)
        
        self.calc_screen_xy = (50, 10)
        self.calc_screen = pygame.Rect(self.calc_screen_xy[0], self.calc_screen_xy[1], self.screen.get_width() - 100, self.button_size)

# --------------------------------------- Draws all Buttons -------------------------------------- #
    def draw(self):
        """
        Displays all the buttons to screen, renders the button text by calling the sub-procedure draw_text().

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
                
        pygame.draw.rect(self.screen, self.colour, self.button_1)
        pygame.draw.rect(self.screen, self.colour, self.button_2)
        pygame.draw.rect(self.screen, self.colour, self.button_3)
        pygame.draw.rect(self.screen, self.colour, self.button_4)
        pygame.draw.rect(self.screen, self.colour, self.button_5)
        pygame.draw.rect(self.screen, self.colour, self.button_6)
        pygame.draw.rect(self.screen, self.colour, self.button_7)
        pygame.draw.rect(self.screen, self.colour, self.button_8)
        pygame.draw.rect(self.screen, self.colour, self.button_9)
        pygame.draw.rect(self.screen, self.colour, self.button_add)
        pygame.draw.rect(self.screen, self.colour, self.button_subtract)
        pygame.draw.rect(self.screen, self.colour, self.button_multiply)
        pygame.draw.rect(self.screen, self.colour, self.button_divide)
        pygame.draw.rect(self.screen, self.colour, self.button_calc)
        pygame.draw.rect(self.screen, self.colour, self.calc_screen)

        self.draw_text(f"{self.button_command[0]}", self.button_1_xy[0] + self.button_size // 2, self.button_1_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[1]}", self.button_2_xy[0] + self.button_size // 2, self.button_2_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[2]}", self.button_3_xy[0] + self.button_size // 2, self.button_3_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[3]}", self.button_4_xy[0] + self.button_size // 2, self.button_4_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[4]}", self.button_5_xy[0] + self.button_size // 2, self.button_5_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[5]}", self.button_6_xy[0] + self.button_size // 2, self.button_6_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[6]}", self.button_7_xy[0] + self.button_size // 2, self.button_7_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[7]}", self.button_8_xy[0] + self.button_size // 2, self.button_8_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[8]}", self.button_9_xy[0] + self.button_size // 2, self.button_9_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[9]}", self.button_add_xy[0] + self.button_size // 2, self.button_add_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[10]}", self.button_subtract_xy[0] + self.button_size // 2, self.button_subtract_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[11]}", self.button_multiply_xy[0] + self.button_size // 2, self.button_multiply_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[12]}", self.button_divide_xy[0] + self.button_size // 2, self.button_divide_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[13]}", self.button_calc_xy[0] + self.button_size // 2, self.button_calc_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.result}", self.screen.get_width() // 2, self.calc_screen_xy[1] + self.button_size // 2)
                
        pygame.display.update()

# ---------------------------------------- Draws all Text ---------------------------------------- #
    def draw_text(self, text, x, y):
        """
        Displays all the buttons to screen, renders the button text by calling the sub-procedure draw_text().

        Parameters
        ----------
            text: str
                The button's text.
            x: int
                The text's x position.
            y: int
                The text's y position.

        Returns
        -------
            None
        """
        
        textobj = self.font.render(text, 1, self.text_colour)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        self.screen.blit(textobj, textrect)

# --------------------------------------- Checks User Input -------------------------------------- #
    def is_clicked(self):
        """
        Determines whether a button is clicked, or if the esc or exit keys are clicked.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        
        mousex, mousey = pygame.mouse.get_pos()

        if self.button_1.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[0]

        elif self.button_2.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[1]
                
        elif self.button_3.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[2]

        elif self.button_4.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[3]

        elif self.button_5.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[4]
                
        elif self.button_6.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[5]

        elif self.button_7.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[6]

        elif self.button_8.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[7]
                
        elif self.button_9.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[8]

        elif self.button_add.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[9]

        elif self.button_subtract.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[10]
                
        elif self.button_multiply.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[11]

        elif self.button_divide.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[12]
                
        elif self.button_calc.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[13]

        self.click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
