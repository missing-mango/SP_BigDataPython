# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:01:00 2023

@author: patel_S
"""
import csv
ANSI_PURPLE = "\033[1;35m"
ANSI_RED = "\033[1;31m"
ANSI_RESET = "\033[0m"
# import data
neighborhood = []
species = []
date = []
edible = []
fruit = []
speciesUnique = []
frequency = []
fruitUnique = []
areaUnique = []
edibleBool = []


def data():
    with open("C:\\Users\\patel_S\\Documents\\sanya\\Trees.csv") as dataFile:
        reader = csv.reader(dataFile)
        for row in reader:
            a = row[1]
            neighborhood.append(a)
            b = row[4]
            species.append(b)
            c = row[10]
            date.append(c)
            d = row[12]
            edible.append(d)
            e = row[13]
            fruit.append(e)
    neighborhood.pop(0)
    species.pop(0)
    date.pop(0)
    edible.pop(0)
    fruit.pop(0)
    # turns the edible list into a boolean list
    for i in range(len(edible)):
        if edible[i] == "TRUE":
            edibleBool.append(True)
        else:
            edibleBool.append(False)


def duplicates(lists, listsUnique):
    for x in lists:
        if x not in listsUnique:
            listsUnique.append(x)  # finds the unique values in species list


# a: prints out all types of trees and the fruit that they give
def fruitBearing():
    duplicates(species, speciesUnique)
    print("{:<28} {:<20}".format(ANSI_PURPLE +
          "Type of Tree", "\t\tFruit Given" + ANSI_RESET))
    for x in speciesUnique:
        index = species.index(x)
        if edibleBool[index] == True:
            print("{:<28} {:<20}".format(x, fruit[index]))
# for every value in speciesUnique, the index of that value in species list is stored in a variable called index
# then if the index of edibleBool is true, the name of that species and fruit are printed


# b: different types of trees + number of that tree in edmonton
def types():
    duplicates(species, speciesUnique)
    print("{:<28} {:<20}".format(ANSI_PURPLE +
          "Type of Tree", "\t\tAmount of Each Tree" + ANSI_RESET))
    for i in range(len(speciesUnique)):
        # counts the frequency of every element in the speciesUnique list
        print("{:<28} {:<5}".format(
            speciesUnique[i], species.count(speciesUnique[i])))


# c: when oldest and newest trees were planted
def datePlanted():
    numMax = str(date.count(max(date)))
    numMin = str(date.count(min(date)))
    print(ANSI_PURPLE + "The newest trees were planted on: " + ANSI_RESET + max(date))
    print(ANSI_PURPLE + "The number of trees planted on this day is: " +
          ANSI_RESET + numMax)
    print(ANSI_PURPLE + "The oldest trees were planted on: " + ANSI_RESET + min(date))
    print(ANSI_PURPLE + "The number of trees planted on this day is: " +
          ANSI_RESET + numMin)


# d: all types of fruit
def typesFruit():
    duplicates(fruit, fruitUnique)
    fruitUnique.pop(0)
    print("{:<28} {:<20}".format(ANSI_PURPLE +
          "Type of Fruit", "\t\tAmount of Trees that Give the Fruit" + ANSI_RESET))
    for i in range(len(fruitUnique)):
        print("{:<28} {:<10}".format(
            fruitUnique[i], fruit.count(fruitUnique[i])))


# e: areas and amount of trees they have
def mostLeast():
    numTrees = []
    duplicates(neighborhood, areaUnique)
    print("{:<35} {:<20}".format(ANSI_PURPLE +
          "Neighborhood", "\t\tAmount of Trees in Neighborhood" + ANSI_RESET))
    for i in range(len(areaUnique)):
        numTrees.append(neighborhood.count(areaUnique[i]))
        print("{:<40} {:<10}".format(areaUnique[i], numTrees[i]))
    x = numTrees.index(max(numTrees))
    y = numTrees.index(min(numTrees))
    print(ANSI_PURPLE + "The most amount of trees are planted in:  " + ANSI_RESET +
          areaUnique[x] + " with " + str(numTrees[x]) + " trees.")
    print(ANSI_PURPLE + "The least amount of trees are planted in: " + ANSI_RESET +
          areaUnique[y] + " with " + str(numTrees[y]) + " tree.")


def search():
    dupLocation = []
    dup = []
    duplicates(species, speciesUnique)
    print(ANSI_PURPLE + "TREE MENU" + ANSI_RESET)
    for i in range(len(speciesUnique)):
        print(speciesUnique[i])
    found = False
    while (not found):
        print("Pick a tree to learn more about")
        choiceSearch = input("Your choice is: ")
        for x in range(len(speciesUnique)):
            if choiceSearch == speciesUnique[x]:
                found = True
                print("")
                # print out name of choice
                print(ANSI_PURPLE + "Species: " + ANSI_RESET + choiceSearch)
                # how many of this species are in edmonton
                num = str(species.count(choiceSearch))
                print(ANSI_PURPLE + "There is " + ANSI_RESET +
                      num + " " + choiceSearch + " trees")
                # all locations of this species
                list2 = [i for i in range(
                    len(species)) if species[i] == choiceSearch]
                for i in list2:
                    # adds all locations of tree to dup list
                    dup.append(neighborhood[i])
                duplicates(dup, dupLocation)
                print(
                    ANSI_PURPLE + "This type of tree can be found at the following locations: " + ANSI_RESET)
                for i in range(len(dupLocation)):
                    print(dupLocation[i])
                # fruit bearing? (if so, what fruit?)
                for i in list2:
                    if edibleBool[i] == True:
                        print(ANSI_PURPLE + "This tree gives the fruit: " +
                              ANSI_RESET + fruit[i])
                        break  # prevents the statement from being printed out i times
                    if edibleBool[i] == False:
                        print(ANSI_PURPLE +
                              "This tree does not give fruit." + ANSI_RESET)
                        break  # prevents the statement from being printed out i times

        if not found:
            print(ANSI_RED + "Whoops, we don't have that tree in Edmonton!" + ANSI_RESET)
