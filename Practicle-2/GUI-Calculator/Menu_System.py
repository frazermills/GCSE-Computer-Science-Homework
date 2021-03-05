import pygame

class Menu:
    def __init__(self, screen, clock, button_colour, text_colour, font, result):
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
        self.title = "Calculator"

    def draw_text(self, text, x, y):
        textobj = self.font.render(text, 1, self.text_colour)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        self.screen.blit(textobj, textrect)

    def update(self):
        mousex, mousey = pygame.mouse.get_pos()

        button_1_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 150, (self.screen.get_height() // 2) - 100)
        button_1 = pygame.Rect(button_1_xy[0], button_1_xy[1], self.button_size, self.button_size)

        button_2_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 50, (self.screen.get_height() // 2) - 100)
        button_2 = pygame.Rect(button_2_xy[0], button_2_xy[1], self.button_size, self.button_size)

        button_3_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 50, (self.screen.get_height() // 2) - 100)
        button_3 = pygame.Rect(button_3_xy[0], button_3_xy[1], self.button_size, self.button_size)

        button_4_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 150, (self.screen.get_height() // 2))
        button_4 = pygame.Rect(button_4_xy[0], button_4_xy[1], self.button_size, self.button_size)

        button_5_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 50, (self.screen.get_height() // 2))
        button_5 = pygame.Rect(button_5_xy[0], button_5_xy[1], self.button_size, self.button_size)

        button_6_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 50, (self.screen.get_height() // 2))
        button_6 = pygame.Rect(button_6_xy[0], button_6_xy[1], self.button_size, self.button_size)

        button_7_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 150, (self.screen.get_height() // 2) + 100)
        button_7 = pygame.Rect(button_7_xy[0], button_7_xy[1], self.button_size, self.button_size)

        button_8_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) - 50, (self.screen.get_height() // 2) + 100)
        button_8 = pygame.Rect(button_8_xy[0], button_8_xy[1], self.button_size, self.button_size)

        button_9_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 50, (self.screen.get_height() // 2) + 100)
        button_9 = pygame.Rect(button_9_xy[0], button_9_xy[1], self.button_size, self.button_size)

        button_add_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 150, (self.screen.get_height() // 2) - 100)
        button_add = pygame.Rect(button_add_xy[0], button_add_xy[1], self.button_size, self.button_size)

        button_subtract_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 150, (self.screen.get_height() // 2))
        button_subtract = pygame.Rect(button_subtract_xy[0], button_subtract_xy[1], self.button_size, self.button_size)

        button_multiply_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 150, (self.screen.get_height() // 2) + 100)
        button_multiply = pygame.Rect(button_multiply_xy[0], button_multiply_xy[1], self.button_size, self.button_size)

        button_divide_xy = ((self.screen.get_width() // 2) - (self.button_size // 2) + 150, (self.screen.get_height() // 2) + 200)
        button_divide = pygame.Rect(button_divide_xy[0], button_divide_xy[1], self.button_size, self.button_size)

        button_calc_xy  = ((self.screen.get_width() // 2) - (self.button_size // 2) + 50, (self.screen.get_height() // 2) + 200)
        button_calc = pygame.Rect(button_calc_xy[0], button_calc_xy[1], self.button_size, self.button_size)
        
        calc_screen_xy = (50, 10)
        calc_screen = pygame.Rect(calc_screen_xy[0], calc_screen_xy[1], self.screen.get_width() - 100, self.button_size)

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
                
        elif button_calc.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[13]
                
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
        pygame.draw.rect(self.screen, self.colour, button_calc)
        pygame.draw.rect(self.screen, self.colour, calc_screen)

        self.draw_text(f"{self.button_command[0]}", button_1_xy[0] + self.button_size // 2, button_1_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[1]}", button_2_xy[0] + self.button_size // 2, button_2_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[2]}", button_3_xy[0] + self.button_size // 2, button_3_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[3]}", button_4_xy[0] + self.button_size // 2, button_4_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[4]}", button_5_xy[0] + self.button_size // 2, button_5_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[5]}", button_6_xy[0] + self.button_size // 2, button_6_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[6]}", button_7_xy[0] + self.button_size // 2, button_7_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[7]}", button_8_xy[0] + self.button_size // 2, button_8_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[8]}", button_9_xy[0] + self.button_size // 2, button_9_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[9]}", button_add_xy[0] + self.button_size // 2, button_add_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[10]}", button_subtract_xy[0] + self.button_size // 2, button_subtract_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[11]}", button_multiply_xy[0] + self.button_size // 2, button_multiply_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[12]}", button_divide_xy[0] + self.button_size // 2, button_divide_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.button_command[13]}", button_calc_xy[0] + self.button_size // 2, button_calc_xy[1] + self.button_size // 2)
        self.draw_text(f"{self.result}", self.screen.get_width() // 2, calc_screen_xy[1] + self.button_size // 2)
                
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
