# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:59:14 2023

@author: patel_S
"""
import functions
# ansi variables for colour
ANSI_RED = "\033[1;31m"
ANSI_GREEN = "\033[1;32m"
ANSI_RESET = "\033[0m"

# refers to the lists created in functions module (telling the code that the lists are equal to the lists creating in the importing data module)
functions.data()
neighborhood, species, date, edible, fruit = functions.neighborhood, functions.species, functions.date, functions.edible, functions.fruit
'''
# testing to see if everything is properly stored:
for i in range(len(neighborhood)):
    print("{:<28} {:<28} {:<12} {:<7} {:<25}".format(
        neighborhood[i], species[i], date[i], edible[i], fruit[i]))
'''
choice = input("To learn more about the trees in Edmonton, press enter!")
while (choice != "exit"):
    print("\nType the number of the algorithm you would like to run. Your choices are:\n" +
          "\n\t a) Fruit Bearing Trees - print out all types of trees that give fruit" +
          "\n\t b) Different Types of Trees - print out the number of each type of tree" +
          "\n\t c) Date planted - print out when the oldest and newest trees were planted" +
          "\n\t d) All Types of Fruit - print out all possible types of fruit" +
          "\n\t e) Most to Least Trees - print out areas and the amount of trees they have" +
          "\n\t f) Search the Data - input a tree from the menu to learn more about it" +
          # enter all other algorithm options
          "\n\t exit - terminate program")
    choice = input("\nYour choice is: ")
    print("")
    if choice == "a":
        functions.fruitBearing()
    elif choice == "b":
        functions.types()
    elif choice == "c":
        functions.datePlanted()
    elif choice == "d":
        functions.typesFruit()
    elif choice == "e":
        functions.mostLeast()
    elif choice == "f":
        functions.search()
    else:
        if choice != "exit":
            print(ANSI_RED + "Invalid input\n" + ANSI_RESET)


print(ANSI_GREEN + "Application has been exited" + ANSI_RESET)
