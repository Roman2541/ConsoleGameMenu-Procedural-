import os  # Both used solely for file I/O
import csv #
from character import *

def addCharacter(): 
    character = [userName(), userRole(), userWealth(), userRace(), userSkill()] # Instantiating a character based on user input
    if character[1] == "warrior":
        character.append(userWeapon())
        character.append(userArmour())
    elif character[1] == "mage": 
        character.append(userSpell()) 
        character.append(userMana())
    characters.append(character) # Adds new character to global array

def listCharacters():
    count = 0
    for character in characters: # Iterating through global array
        count += 1
        print(str(count) + ". " + character[0]) # e.g. "1. Name"
    if count == 0:
        print("No Characters found.")

def searchCharacterByName():
    searchTerm = "" # Defining variable in outer scope for use later on
    while True:
        searchTerm = input("Please Enter an alphanumerical username with 16 or less characters: ").lower()
        if searchTerm.isalnum() and len(searchTerm) <= 16: 
            break
    for character in characters:
        if character[0] == searchTerm:
             printDetails(character) # Details are printed when a name matching the search term is found
             return
    print("Character does not Exist.")

def displayTotalWealth():
    totalWealth = 0
    for character in characters:
        totalWealth += int(character[2])
    print("Total Wealth:", totalWealth)

def saveToFile():
    with open(os.path.join(os.path.dirname(__file__), "characters.csv"), 'w', newline = '') as csvfile: # Opens file from absolute path with write permissions and is assigned to csvfile
        writer = csv.writer(csvfile, delimiter = ',') # Initates csv.writer
        for character in characters:
            writer.writerow([character[0]] + 
                            [character[1]] + 
                            [character[2]] + 
                            [character[3]] + 
                            [character[4]] + 
                            [character[5]] + # Dynamically gets extra members based on whether role is warrior or mage
                            [character[6]])  #

def loadFromFile():
    characters.clear()
    with open(os.path.join(os.path.dirname(__file__), "characters.csv"), 'r', newline = '') as csvfile: # Opens the file with read permissions instead of write
        reader = csv.reader(csvfile, delimiter = ',') # Initates csv.reader
        for row in reader:
            character = [row[0], row[1], row[2], row[3], row[4]]
            if character[1] == "warrior":                         
                character.append(row[5])
                character.append(row[6])
            elif character[1] == "mage": 
                character.append(row[5])
                character.append(row[6])
            characters.append(character)
        
def mainMenu():
    choice = 0
    while True:
        try:
            choice = int(input("\n1 - Add a Character\n" +
                               "2 - List all Characters\n" +
                               "3 - Search for Characters by Name\n" +
                               "4 - Total Wealth of all the Characters\n" +
                               "5 - Save Characters to a File\n" +
                               "6 - Load Characters from a File\n" +
                               "0 - Exit Application\n" +
                               "Please Enter Your Choice: "))
            if choice >= 0 and choice <= 6:
                break
        except:
            pass

    match choice:
        case 0: exit()
        case 1: addCharacter()
        case 2: listCharacters() 
        case 3: searchCharacterByName() 
        case 4: displayTotalWealth()
        case 5: saveToFile()
        case 6: loadFromFile()
        case _: exit() # If somehow no other cases are hit exit is the default action