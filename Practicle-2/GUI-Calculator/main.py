import pygame, Menu_System

def main():
    WIDTH = 400
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    fps = 25
    result = 0
    
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Caculator - by Frazer Mills")
    clock = pygame.time.Clock()
    text_font = pygame.font.SysFont("Arial", 40)
    text_colour = BLACK
    button_colour = WHITE
    
    while True:
        nums, operator = menu_handler(screen, clock, WHITE, text_colour, text_font, result)
        result = operation_handler(nums, operator)
        pygame.display.update()
        clock.tick(fps)

def menu_handler(screen, clock, button_colour, text_colour, text_font, result):
    menu = Menu_System.Menu(screen, clock, button_colour, text_colour, text_font, result)
    operator = None
    nums = []
    
    while menu.option != "calc":
        menu.option = None
        menu.update()
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

def operation_handler(nums, operator):
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

if __name__ == "__main__":
    main()
