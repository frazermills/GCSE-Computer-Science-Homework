# This is an example menu system made by my teacher

menu = "What would you like:\n\
        1. A complement?\n\
        2. An insult?\n\
        3. A proverb\n\
        4. An idiom\n\
        9. Quit\n"

x = int(input(menu))

if x == 1:
    print("You look lovely today!")
elif x == 2:
    print("You smell funny.")
elif x == 3:
    print("Two wrongs don't make a right. But three lefts do...")
elif x == 4:
    print("The pen is mightier than the sword.")
elif x == 9:
    print("Goodbye!!!")
