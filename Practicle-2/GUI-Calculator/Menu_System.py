import pygame

class Menu:
    def __init__(self, screen, clock, colour):
        self.screen = screen
        self.clock = clock
        self.colour = colour
        self.click = False
        self.button_size = 100
        self.button_width = 75
        self.button_height = 75
        self.option = None
        self.button_command = ["button 1", "button 2", "button 3", "button 4", "button 5", "button 6", "button 7", "button 8", "button 9", "add", "subtract", "multiply", "divide"]
        self.title = "Calculator"

    def setup(self):
        pass
    
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()

        button_1_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) - 150, (self.screen.get_height() // 2) - 100)
        button_1 = pygame.Rect(button_1_xy[0], button_1_xy[1], self.button_width, self.button_height)

        button_2_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) - 50, (self.screen.get_height() // 2) - 100)
        button_2 = pygame.Rect(button_2_xy[0], button_2_xy[1], self.button_width, self.button_height)

        button_3_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) + 50, (self.screen.get_height() // 2) - 100)
        button_3 = pygame.Rect(button_3_xy[0], button_3_xy[1], self.button_width, self.button_height)

        button_4_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) - 150, (self.screen.get_height() // 2))
        button_4 = pygame.Rect(button_4_xy[0], button_4_xy[1], self.button_width, self.button_height)

        button_5_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) - 50, (self.screen.get_height() // 2))
        button_5 = pygame.Rect(button_5_xy[0], button_5_xy[1], self.button_width, self.button_height)

        button_6_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) + 50, (self.screen.get_height() // 2))
        button_6 = pygame.Rect(button_6_xy[0], button_6_xy[1], self.button_width, self.button_height)

        button_7_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) - 150, (self.screen.get_height() // 2) + 100)
        button_7 = pygame.Rect(button_7_xy[0], button_7_xy[1], self.button_width, self.button_height)

        button_8_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) - 50, (self.screen.get_height() // 2) + 100)
        button_8 = pygame.Rect(button_8_xy[0], button_8_xy[1], self.button_width, self.button_height)

        button_9_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) + 50, (self.screen.get_height() // 2) + 100)
        button_9 = pygame.Rect(button_9_xy[0], button_9_xy[1], self.button_width, self.button_height)

        button_add_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) + 150, (self.screen.get_height() // 2) - 100)
        button_add = pygame.Rect(button_add_xy[0], button_add_xy[1], self.button_width, self.button_height)

        button_subtract_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) + 150, (self.screen.get_height() // 2))
        button_subtract = pygame.Rect(button_subtract_xy[0], button_subtract_xy[1], self.button_width, self.button_height)

        button_multiply_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) + 150, (self.screen.get_height() // 2) + 100)
        button_multiply = pygame.Rect(button_multiply_xy[0], button_multiply_xy[1], self.button_width, self.button_height)

        button_divide_xy = ((self.screen.get_width() // 2) - (self.button_width // 2) + 150, (self.screen.get_height() // 2) + 200)
        button_divide = pygame.Rect(button_divide_xy[0], button_divide_xy[1], self.button_width, self.button_height)

        if button_1.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[0]

        elif button_2.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[1]
                
        elif button_3.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[2]

        elif button_4.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[3]

        elif button_5.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[4]
                
        elif button_6.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[5]

        elif button_7.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[6]

        elif button_8.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[7]
                
        elif button_9.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[8]

        elif button_add.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[9]

        elif button_subtract.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[10]
                
        elif button_multiply.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[11]

        elif button_divide.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[12]

        pygame.draw.rect(self.screen, self.colour, button_1)
        pygame.draw.rect(self.screen, self.colour, button_2)
        pygame.draw.rect(self.screen, self.colour, button_3)
        pygame.draw.rect(self.screen, self.colour, button_4)
        pygame.draw.rect(self.screen, self.colour, button_5)
        pygame.draw.rect(self.screen, self.colour, button_6)
        pygame.draw.rect(self.screen, self.colour, button_7)
        pygame.draw.rect(self.screen, self.colour, button_8)
        pygame.draw.rect(self.screen, self.colour, button_9)
        pygame.draw.rect(self.screen, self.colour, button_add)
        pygame.draw.rect(self.screen, self.colour, button_subtract)
        pygame.draw.rect(self.screen, self.colour, button_multiply)
        pygame.draw.rect(self.screen, self.colour, button_divide)

        pygame.display.update()

    def is_clicked(self):
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
