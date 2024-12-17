characters = []

def printDetails(character): 
    print("Character Name: " + character[0])
    print("Character Role: " + character[1])
    print("Character Wealth: " + character[2])
    print("Character Race: " + character[3])
    print("Character Skill: " + character[4])
    if character[1] == "warrior":
        print("Character Weapon: " + character[5])
        print("Character Armour: " + character[6])
    elif character[1] == "mage":
        print("Character Spell: " + character[5])
        print("Character Mana: " + character[6])

def userName():
    while True:
        name = input("Please Enter an alphanumerical username with 16 or less characters: ")
        isDuplicate = False
        for character in characters: # Iteration through the array is necessary to ensure no duplicates
            if character[0] == name:
                isDuplicate = True
        if name.isalnum() and len(name) <= 16 and not isDuplicate: 
            return name
def userRole():
    while True:
        role = input("Please Enter your Role (Warrior / Mage): ").lower()
        if role == "warrior" or role == "mage":
            return role
def userWealth():
    while True:
        try:
            wealth = int(input("Please Enter a Wealth greater than or equal to 0: "))
            if wealth >= 0:
                return str(wealth) # Converting the return to a string so it can be used more easily to print
        except:
            pass
def userRace():
    while True:
        race = input("Please Enter your Race (Human / Dwarf / Elf): ").lower()
        if race == "human" or race == "dwarf" or race == "elf":
            return race
def userSkill():
    while True:
        try:
            skill = int(input("Please Enter your Skill Level (1 - 5): "))
            if skill > 0 and skill < 6:
                return str(skill)
        except:
            pass

# Role based functions 
def userWeapon():
    while True:
        weapon = input("Please Select your Weapon (Sword / Axe) ").lower()
        if weapon == "sword" or weapon == "axe":
            return weapon
def userArmour():
    while True:
        armour = input("Please Select your Weapon (Chainmail / Plate) ").lower()
        if armour == "chainmail" or armour == "plate":
            return armour
def userSpell():
    while True:
        spell = input("Please Select your Weapon (Fireball / Lightning) ").lower()
        if spell == "fireball" or spell == "lightning":
            return spell
def userMana():
    while True:
        try:
            mana = int(input("Please Enter your Mana Points (0 - 100): "))
            if mana >= 0 and mana <= 100:
                return str(mana)
        except:
            pass