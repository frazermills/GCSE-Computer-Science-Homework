import pygame, Menu_System

def main():
    WIDTH = 400
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    fps = 25
    
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    text_font = pygame.font.SysFont("Arial", 40)
    text_colour = BLACK
    button_colour = WHITE
    
    while True:
        menu_handler(screen, clock, WHITE, text_colour, text_font)
        pygame.display.update()
        clock.tick(fps)

def menu_handler(screen, clock, button_colour, text_colour, text_font):
    menu = Menu_System.Menu(screen, clock, button_colour, text_colour, text_font)
    while menu.option == None:
        menu.update()
        menu.is_clicked()

        if menu.option == "1":
            print("button 1 clicked")
            
        elif menu.option == "2":
            print("button 2 clicked")

        elif menu.option == "3":
            print("button 3 clicked")

        elif menu.option == "4":
            print("button 4 clicked")

        elif menu.option == "5":
            print("button 5 clicked")

        elif menu.option == "6":
            print("button 6 clicked")

        elif menu.option == "7":
            print("button 7 clicked")

        elif menu.option == "8":
            print("button 8 clicked")

        elif menu.option == "9":
            print("button 9 clicked")

        elif menu.option == "+":
            print("add button clicked")

        elif menu.option == "-":
            print("subtract button clicked")

        elif menu.option == "*":
            print("multiply button clicked")

        elif menu.option == "/":
            print("divide button clicked")


if __name__ == "__main__":
    main()
