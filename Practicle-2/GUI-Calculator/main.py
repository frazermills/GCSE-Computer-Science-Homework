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
    while True:
        menu_handler(screen, clock, WHITE)
        pygame.display.update()
        clock.tick(fps)
    

def menu_handler(screen, clock, colour):
    menu = Menu_System.Menu(screen, clock, colour)
    while menu.option == None:
        menu.update()
        menu.is_clicked()

        if menu.option == "button 1":
            print("button 1 clicked")
            
        elif menu.option == "button 2":
            print("button 2 clicked")

        elif menu.option == "button 3":
            print("button 3 clicked")

        elif menu.option == "button 4":
            print("button 4 clicked")

        elif menu.option == "button 5":
            print("button 5 clicked")

        elif menu.option == "button 6":
            print("button 6 clicked")

        elif menu.option == "button 7":
            print("button 7 clicked")

        elif menu.option == "button 8":
            print("button 8 clicked")

        elif menu.option == "button 9":
            print("button 9 clicked")

        elif menu.option == "add":
            print("add button clicked")

        elif menu.option == "subtract":
            print("subtract button clicked")

        elif menu.option == "multiply":
            print("multiply button clicked")

        elif menu.option == "divide":
            print("divide button clicked")


if __name__ == "__main__":
    main()
