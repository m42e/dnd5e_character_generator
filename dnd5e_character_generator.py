#TODO skill versatility, proficeincy flag, custom cap, and size

from random import randint

class Player:
    def  __init__(self):
        self.name = None
        self.className = None
        self.str = None
        self.dex = None
        self.con = None
        self.int = None
        self.wis = None
        self.cha = None
        self.hp = 0
        self.str_mod = None
        self.dex_mod = None
        self.con_mod = None
        self.int_mod = None
        self.wis_mod = None
        self.cha_mod = None
        self.init = None
        self.speed = None
        self.prof_bonus = None
        self.race = None
        self.save = None
        self.prof = []
        self.skills = {"Acrobatics":0, "Animal Handling":0, "Arcana":0, "Athletics":0, "Deception":0, "History":0, "Insight":0, "Intimidation":0, "Investigation":0, "Medicine":0, "Nature":0, "Perception":0, "Performance":0, "Persuasion":0, "Religion":0, "Sleight of Hand":0, "Stealth":0, "Survival":0}
        self.rec_alignment = []
        self.traits = []
        self.lang = []
        self.size = "Medium"

def best_of_4d6():
    rolls = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
    rolls.remove(min(rolls))
    return sum(rolls)

def random_abil():
    n1 = best_of_4d6()
    n2 = best_of_4d6()
    n3 = best_of_4d6()
    n4 = best_of_4d6()
    n5 = best_of_4d6()
    n6 = best_of_4d6()
    abil = [n1, n2, n3, n4, n5, n6]
    abil.sort(reverse = True)
    print("You rolled the following scores: " + str(abil))
    return abil

def predef_abil():
    abil = [15, 14, 13, 12, 10, 8]
    print("You have the following scores to place as you please: " + str(abil))
    return abil

def custom_abil():
    new_player.str = int(input("What is your strength: "))
    new_player.dex = int(input("What is your dexterity: "))
    new_player.con = int(input("What is your constitution: "))
    new_player.int = int(input("What is your intelligence: "))
    new_player.wis = int(input("What is your wisdom: "))
    new_player.cha = int(input("What is your charisma: "))

def abil_input(abil):
    picked = []
    while(len(picked) < 6):
        choice = input("Will " + str(abil[len(picked)]) + " be your (S)trength, (D)exterity, (C)onstitution, (I)ntelligence, (W)isdom, or (Ch)arisma: ").upper()
        if choice == 'S' and choice not in picked: 
            new_player.str = abil[len(picked)]
            picked.append('S')
        elif choice == 'D' and choice not in picked:     
            new_player.dex = abil[len(picked)]
            picked.append('D')
        elif choice == 'C' and choice not in picked: 
            new_player.con = abil[len(picked)]
            picked.append('C')
        elif choice == 'I' and choice not in picked: 
            new_player.int = abil[len(picked)]
            picked.append('I')
        elif choice == 'W' and choice not in picked: 
            new_player.wis = abil[len(picked)]
            picked.append('W')
        elif choice == 'CH' and choice not in picked: 
            new_player.cha = abil[len(picked)]
            picked.append('CH')
        else: print("Invalid option")

def abil_menu():
    print("")
    print("A brief explanation of ability scores in terms of a tomato\nStrength is your ability to crush a tomato\nDexterity is the ability to dodge a tomato thrown at you\nConstitution is the ability to eat a rotten tomato and not get sick\nIntelligence is knowing a tomato is a fruit\nWisdom is knowing not to put a tomato in a fruit salad\nCharisma is being able to sell a tomato based fruit salad\nFor more information see Pg 14\n")
    while True:
        choice = input("How would you like to determine your ability scores? (R)andom, (P)redetermined, (C)ustom, or (D)escription: ").upper()
        if choice == 'R':
            abil_input(random_abil())
            break;
        elif choice == 'P':
            abil_input(predef_abil())
            break;
        elif choice == 'C': 
            custom_abil()
            break;
        elif choice == 'D':
            print("\nRandon will roll 4d6 and add up the 3 highest rolls to give you six numbers to distribute your ability scores however you would like\nPredefined will give you the numbers 15, 14, 13, 12, 10, 8, and you may distribute them amongst your ability scores however you choose\nCustom will allow you to input whatever numbers you like for your ability scores\n")
        else: print("Invalid option")

def add_distinct(lst):
    for word in lst:
        if word not in new_player.prof:
            new_player.prof.append(word)

def new_lang():
    while True:
        choice = input("What langauge would you like to add to your character Dwarvish, Elvish, Giant, Gnomish, Goblin, Halfling, Orc, Abyssal, Celestial, Draconic, Deep Speech, Infernal, Primordial, Undercommon, Sylvan, Druidic: ").upper()
        if choice == 'DWARVISH':
            return "Dwarvish"
            break;
        elif choice == 'ELVISH':
            return "Elvish"
            break;
        elif choice == 'GIANT': 
            return "Giant"
            break;
        elif choice == 'GNOMISH': 
            return "Gnomish"
            break;
        elif choice == 'GOBLIN': 
            return "Goblin"
            break;
        elif choice == 'HALFLING': 
            return "Halfling"
            break;
        elif choice == 'ORC': 
            return "Orc"
            break;
        elif choice == 'ABYSSAL': 
            return "Abyssal"
            break;
        elif choice == 'CELESTIAL': 
            return "Celestial"
            break;
        elif choice == 'DRACONIC': 
            return "Draconic"
            break;
        elif choice == 'DEEP SPEECH': 
            return "Deep Speech"
            break;
        elif choice == 'INFERNAL': 
            return "Infernal"
            break;
        elif choice == 'PRIMORDIAL': 
            return "Primordial"
            break;
        elif choice == 'SYLVAN': 
            return "Sylvan"
            break;
        elif choice == 'UNDERCOMMON': 
            return "Undercommon"
            break;
        elif choice == 'DRUIDIC': 
            return "Druidic"
            break;
        else: print("Invalid option")

def race_menu():
    print("")
    print("Races:")
    print("1) Dwarf (pg 18) // Constitution +2")
    print("2) Elf (pg 21) // Dexterity +2")
    print("3) Halfling (pg 26) // Dexterity +2")
    print("4) Human (pg 29) // Each ability score +1")
    print("5) Dragonborn (pg 32) // Strength +2, Charisma +1")
    print("6) Gnome (pg 35) // Intelligence +2")
    print("7) Half-Elf (pg 38) // Charisma +2, +1 to two other scores of your choice")
    print("8) Half-Orc (pg 40) // Strength +2, Constitution +1")
    print("9) Tiefling (pg 42) // Intelligence +1, Charisma +2")
        
    while True:
        choice = input("Choose from the above races: ")
        if choice == '1':
            new_player.con += 2
            new_player.speed = 25
            new_player.lang += ["Dwarvish","Common"]
            new_player.traits += ["Dwarven Resilience","Dwarven Combat Training","Tool Proficiency","Stonecunning"]
            new_player.rec_alignment += "Lawful Good"
            prof = ["Battleaxe", "Handaxe", "Throwing Hammer", "Warhammer"]
            add_distinct(prof)
            while True:
                choice = input("Would you like to be a (H)ill Dwarf //Wisdom +1 and Hit Points +1// or a (M)ountain Dwarf //Strength +2//: ").upper()
                if choice == 'H':
                    new_player.race = "Dwarf (Hill Dwarf)"
                    new_player.wis += 1
                    new_player.hp += 1
                    new_player.traits += "Dwarven Toughness"
                    break;
                elif choice == 'M':
                    new_player.race = "Dwarf (Mountain Dwarf)"
                    new_player.str += 2
                    prof = ["Light Armor", "Medium Armor"]
                    add_distinct(prof)
                    new_player.traits += "Dwarven Armor Training"
                    break;
                else: print("Invalid option")
            break;
        elif choice == '2':
            new_player.speed = 30
            new_player.dex += 2
            new_player.lang += ["Elvish","Common"]
            new_player.traits += ["Darkvision","Keen Senses","Fey Ancestry","Trance"]
            new_player.rec_alignment += "Chaotic Good"
            new_player.skills["Perception"] += 2
            while True:
                choice = input("Would you like to be (H)igh Elf //Intelligence +1//, a (W)ood Elf //Wisdom +1//, or a (D)ark Elf //Charisma +1//: ").upper()
                if choice == 'H':
                    new_player.race = "Elf (High Elf)"
                    new_player.int += 1
                    prof = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
                    add_distinct(prof)
                    new_player.traits += ["Elf Weapon Training","Cantrip","Extra Language"]
                    language = new_lang()
                    while True:
                        if language in new_player.lang:
                            print("Your character already knows that language, please choose another")
                            language = new_lang()
                        else:
                            new_player.lang += [language]
                            break
                    break;
                elif choice == 'W':
                    new_player.race = "Elf (Wood Elf)"
                    new_player.wis += 1
                    new_player.speed = 35
                    prof = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
                    add_distinct(prof)
                    new_player.traits += ["Elf Weapon Training","Fleet of Foot","Mask of the Wild"]
                    break;
                elif choice == 'D':
                    new_player.race = "Elf (Dark Elf)"
                    new_player.cha += 1
                    new_player.rec_alignment = "Chaotic Evil"
                    prof = ["Rapier", "Shortsword", "Hand Crossbow"]
                    add_distinct(prof)
                    new_player.traits += ["Superior Darkvision","Sunlight Sensitivity","Drow Magic","Drow Weapon Training"]
                    break;
                else: print("Invalid option")
            break;
        elif choice == '3':
            new_player.speed = 25
            new_player.dex += 2
            new_player.lang += ["Common", "Halfling"]
            new_player.traits += ["Lucky","Brave","Halfling Nimbleness"]
            new_player.rec_alignment = "Lawful Good"
            while True:
                choice = input("Would you like to be a (L)ightfoot Halfling //Charisma +1// or a (S)tout Halfling //Constitution +1//: ").upper()
                if choice == 'L':
                    new_player.race = "Halfling (Lightfoot)"
                    new_player.cha += 1
                    new_player.traits += ["Naturally Stealthy"]
                    break;
                elif choice == 'S':
                    new_player.race = "Halfling (Stout)"
                    new_player.con += 1
                    new_player.traits += ["Stout Resilience"]
                    break;
                else: print("Invalid option")
            break;
        elif choice == '4':
            new_player.speed = 30
            new_player.race = "Human"
            new_player.str += 1
            new_player.dex += 1
            new_player.con += 1
            new_player.int += 1
            new_player.wis += 1
            new_player.cha += 1
            language = new_lang()
            new_player.lang += ["Common",language]
            break;
        elif choice == '5':
            new_player.speed = 30
            new_player.race = "Dragonborn"
            new_player.str += 2
            new_player.cha += 1
            new_player.traits += ["Draconic Ancestry","Breath Weapon","Damage Resistance"]
            new_player.lang += ["Common","Draconic"]
            break;
        elif choice == '6':
            new_player.speed = 25
            new_player.int += 2
            while True:
                new_player.rec_alignment = "Good"
                new_player.traits += ["Darkvision","Gnome Cunning"]
                new_player.lang += ["Common","Gnomish"]
                choice = input("Would you like to be a (F)orest Gnome //Dexterity +1// or a (R)ock Gnome //Charisma +1//: ").upper()
                if choice == 'F':
                    new_player.race = "Gnome (Forest Gnome)"
                    new_player.dex += 1
                    new_player.traits += ["Natural Illusionist","Speak with Small Beasts"]
                    break;
                elif choice == 'R':
                    new_player.race = "Gnome (Rock Gnome)"
                    new_player.con += 1
                    new_player.traits += ["Artificer's Lore","Tinker"]
                    break;
                else: print("Invalid option")
            break;
        elif choice == '7':
            new_player.speed = 30
            count = 0
            new_player.race = "Half-Elf"
            new_player.cha += 2
            new_player.traits += ["Darkvision","Fey Ancestry","Skill Versitility"]
            new_player.rec_alignment = "Chaotic"
            new_player.lang += ["Common", "Elvish"]
            language = new_lang()
            print(language)
            while True:
                if language in new_player.lang:
                    print("Your character already knows that language, please choose another")
                    language = new_lang()
                else:
                    new_player.lang += [language]
                    break
            while count < 2:
                choice = input("Would you like to increase (S)trength, (D)exterity, (C)onstitution, (I)ntelligence, or (W)isdom: ").upper()
                if choice == 'S':
                    new_player.str += 1
                    count += 1
                elif choice == 'D':     
                    new_player.dex += 1
                    count += 1
                elif choice == 'C': 
                    new_player.con += 1
                    count += 1
                elif choice == 'I': 
                    new_player.int += 1
                    count += 1
                elif choice == 'W': 
                    new_player.wis += 1
                    count += 1
                else: print("Invalid option")
            break;
        elif choice == '8':
            new_player.speed = 30
            new_player.race = "Half-Orc"
            new_player.str += 2
            new_player.con += 1
            new_player.rec_alignment = "Chaotic Evil"
            new_player.traits += ["Darkvision","Menacing","Relentless Endurance","Savage Attacks"]
            new_player.lang += ["Common","Orc"]
            break;
        elif choice == '9':
            new_player.speed = 30
            new_player.race = "Tiefling"
            new_player.cha += 2
            new_player.int += 1
            new_player.rec_alignment = "Chaotic"
            new_player.traits += ["Darkvision","Hellish Resistance","Infernal Legacy"]
            new_player.lang += ["Common","Infernal"]
            break;
        else: print("Invalid option")

def class_menu():
    print("")
    print("Classes: ")
    print("1) Barbarian (pg 46) A fierce warrior of primitive background who can enter a battle rage")
    print("2) Bard (pg 49) An inspiring magician whose power echoes the music of creation")
    print("3) Cleric (pg 56) A priestly champion who wields divine magic in service of a higher power")
    print("4) Druid (pg 64) A priest of the Old Faith, wielding the powers of nature-moonlight and the plant growth, fire and lightning-and adopting animal forms")
    print("5) Fighter (pg 70) A master of martial combat, skilled with a variety of weapons and armor")
    print("6) Monk (pg 76) A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection")
    print("7) Paladin (pg 82) A holy warrior bound to a sacred oath")
    print("8) Ranger (pg 89) A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization")
    print("9) Rogue (pg 94) A scoundrel who uses stealth and trickery to overcome obstacles and enemies")
    print("10) Sorcerer (pg 99) A spellcaster who draws on inherent magic from a gift or bloodline")
    print("11) Warlock (pg 105) A wielder of magic that is derived from a bargain with an extraplanar entity")
    print("12) Wizard (pg 112) A scholarly magic-user capable of manipulating the structure of reality")
    
    while True:
        choice = input("Choose from the above classes: ")
        print("Type the full name of a single skill as it appears, then hit [ENTER] before typing the next selection.")
        if choice == '1':
            new_player.className = "Barbarian"
            new_player.hp += randint(1,12) + new_player.con_mod
            prof = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Dexterity, Charisma"
            picked = []
            while len(picked) < 2:
                choice = input("Choose two of the following skills to be trained in Animal Handling, Athletics, Intimidation, Nature, Perception, Survival: ")
                if choice == "Animal Handling" and "Animal Handling" not in picked:
                    picked.append("Animal Handling")
                    new_player.skills["Animal Handling"] += 3
                elif choice == "Athletics" and "Athletics" not in picked:
                    picked.append("Athletics")
                    new_player.skills["Athletics"] += 3
                elif choice == "Intimidation" and "Intimidation" not in picked:
                    picked.append("Intimidation")
                    new_player.skills["Intimidation"] += 3
                elif choice == "Nature" and "Nature" not in picked:
                    picked.append("Nature")
                    new_player.skills["Nature"] += 3
                elif choice == "Perception" and "Perception" not in picked:
                    picked.append("Perception")
                    new_player.skills["Perception"] += 3
                elif choice == "Survival" and "Survival" not in picked:
                    picked.append("Survival")
                    new_player.skills["Survival"] += 3
                else: print("Invalid option")
            break;
        elif choice == '2':
            new_player.className = "Bard"
            new_player.hp += randint(1,8) + new_player.con_mod
            prof = ["Light Armor", "Simple Weapons", "Hand Crossbow", "Longsword", "Rapier", "Shortsword"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Dexterity, Charisma"
            picked = []
            while len(picked) < 3:
                print(new_player.skills)
                choice = input("Choose three skills to be trained in: ")
                if choice in new_player.skills and choice not in picked:
                    picked.append(choice)
                    new_player.skills[choice] += 3
                else: print("Invalid option")
            break;
        elif choice == '3':
            new_player.className = "Cleric"
            new_player.hp += randint(1,8) + new_player.con_mod
            prof = ["Light Armor", "Medium Armor", "Shield", "All Simple Weapons"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Wisdom, Charisma"
            picked = []
            while len(picked) < 2:
                choice = input("Choose two of the following skills to be trained in History, Insight, Medicine, Persuasion, or Religion: ")
                if choice == "History" and "History" not in picked:
                    picked.append("History")
                    new_player.skills["History"] += 3
                elif choice == "Insight" and "Insight" not in picked:
                    picked.append("Insight")
                    new_player.skills["Insight"] += 3
                elif choice == "Medicine" and "Medicine" not in picked:
                    picked.append("Medicine")
                    new_player.skills["Medicine"] += 3
                elif choice == "Persuasion" and "Persuasion" not in picked:
                    picked.append("Persuasion")
                    new_player.skills["Persuasion"] += 3
                elif choice == "Religion" and "Religion" not in picked:
                    picked.append("Religion")
                    new_player.skills["Religion"] += 3
                else: print("Invalid option")
            break;
        elif choice == '4':
            new_player.className = "Druid"
            new_player.hp += randint(1,8) + new_player.con_mod
            prof = ["Light Armor (Non-metal)", "Medium Armor (Non-metal)", "Shield (Non-metal)", "Club", "Dagger", "Dart", "Javelin", "Mace", "Quarterstaff", "Scimtar", "Sickle", "Sling", "Spear"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Intelligence, Wisdom"
            picked = []
            while len(picked) < 2:
                choice = input("Choose two of the following skills to be trained in Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, or Survival: ")
                if choice == "Arcana" and "Arcana" not in picked:
                    picked.append("Arcana")
                    new_player.skills["Arcana"] += 3
                elif choice == "Animal Handling" and "Animal Handling" not in picked:
                    picked.append("Animal Handling")
                    new_player.skills["Animal Handling"] += 3
                elif choice == "Insight" and "Insight" not in picked:
                    picked.append("Insight")
                    new_player.skills["Insight"] += 3
                elif choice == "Medicine" and "Medicine" not in picked:
                    picked.append("Medicine")
                    new_player.skills["Medicine"] += 3
                elif choice == "Nature" and "Nature" not in picked:
                    picked.append("Nature")
                    new_player.skills["Nature"] += 3
                elif choice == "Perception" and "Perception" not in picked:
                    picked.append("Perception")
                    new_player.skills["Perception"] += 3
                elif choice == "Religion" and "Religion" not in picked:
                    picked.append("Religion")
                    new_player.skills["Religion"] += 3
                elif choice == "Survival" and "Survival" not in picked:
                    picked.append("Survival")
                    new_player.skills["Survival"] += 3
                else: print("Invalid option")
            break;
        elif choice == '5':
            new_player.className = "Fighter"
            new_player.hp += randint(1,10) + new_player.con_mod
            prof = ["All Armor", "All Shields", "Simple Weapons", "Martial Weapons"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Strength, Constitution"
            picked = []
            while len(picked) < 2:
                choice = input("Choose two of the following skills to be trained in Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, or Survival: ")
                if choice == "Acrobatics" and "Acrobatics" not in picked:
                    picked.append("Acrobatics")
                    new_player.skills["Acrobatics"] += 3
                elif choice == "Animal Handling" and "Animal Handling" not in picked:
                    picked.append("Animal Handling")
                    new_player.skills["Animal Handling"] += 3
                elif choice == "Insight" and "Insight" not in picked:
                    picked.append("Insight")
                    new_player.skills["Insight"] += 3
                elif choice == "Athletics" and "Athletics" not in picked:
                    picked.append("Athletics")
                    new_player.skills["Athletics"] += 3
                elif choice == "History" and "History" not in picked:
                    picked.append("History")
                    new_player.skills["History"] += 3
                elif choice == "Intimidation" and "Intimidation" not in picked:
                    picked.append("Intimidation")
                    new_player.skills["Intimidation"] += 3
                elif choice == "Perception" and "Perception" not in picked:
                    picked.append("Perception")
                    new_player.skills["Perception"] += 3
                elif choice == "Survival" and "Survival" not in picked:
                    picked.append("Survival")
                    new_player.skills["Survival"] += 3
                else: print("Invalid option")
            break;
        elif choice == '6':
            new_player.className = "Monk"
            new_player.hp += randint(1,8) + new_player.con_mod
            prof = ["Simple Weapons", "Shortsword"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Strength, Dexterity"
            picked = []
            while len(picked) < 2:
                choice = input("Choose two of the following skills to be trained in Acrobatics, Athletics, History, Insight, Religion, Stealth: ")
                if choice == "Acrobatics" and "Acrobatics" not in picked:
                    picked.append("Acrobatics")
                    new_player.skills["Acrobatics"] += 3
                elif choice == "Insight" and "Insight" not in picked:
                    picked.append("Insight")
                    new_player.skills["Insight"] += 3
                elif choice == "Athletics" and "Athletics" not in picked:
                    picked.append("Athletics")
                    new_player.skills["Athletics"] += 3
                elif choice == "History" and "History" not in picked:
                    picked.append("History")
                    new_player.skills["History"] += 3
                elif choice == "Religion" and "Religion" not in picked:
                    picked.append("Religion")
                    new_player.skills["Religion"] += 3
                elif choice == "Stealth" and "Stealth" not in picked:
                    picked.append("Stealth")
                    new_player.skills["Stealth"] += 3
                else: print("Invalid option")
            break;
        elif choice == '7':
            new_player.className = "Paladin"
            new_player.hp += randint(1,10) + new_player.con_mod
            prof = ["All Armor", "All Shields", "Simple Weapons", "Martial Weapons"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Wisdom, Charisma"
            picked = []
            while len(picked) < 2:
                choice = input("Choose two of the following skills to be trained in Athletics, Insight, Intimidation, Medicine, Persuasion, or Religion: ")
                if choice == "Religion" and "Religion" not in picked:
                    picked.append("Religion")
                    new_player.skills["Religion"] += 3
                elif choice == "Persuasion" and "Persuasion" not in picked:
                    picked.append("Persuasion")
                    new_player.skills["Persuasion"] += 3
                elif choice == "Insight" and "Insight" not in picked:
                    picked.append("Insight")
                    new_player.skills["Insight"] += 3
                elif choice == "Athletics" and "Athletics" not in picked:
                    picked.append("Athletics")
                    new_player.skills["Athletics"] += 3
                elif choice == "Medicine" and "Medicine" not in picked:
                    picked.append("Medicine")
                    new_player.skills["Medicine"] += 3
                elif choice == "Intimidation" and "Intimidation" not in picked:
                    picked.append("Intimidation")
                    new_player.skills["Intimidation"] += 3
                else: print("Invalid option")
            break;
        elif choice == '8':
            new_player.className = "Ranger"
            new_player.hp += randint(1,10) + new_player.con_mod
            prof = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Strength, Dexterity"
            picked = []
            while len(picked) < 3:
                choice = input("Choose three of the following skills to be trained in Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, or Survival: ")
                if choice == "Animal Handling" and "Animal Handling" not in picked:
                    picked.append("Animal Handling")
                    new_player.skills["Animal Handling"] += 3
                elif choice == "Insight" and "Insight" not in picked:
                    picked.append("Insight")
                    new_player.skills["Insight"] += 3
                elif choice == "Investigation" and "Investigation" not in picked:
                    picked.append("Investigation")
                    new_player.skills["Investigation"] += 3
                elif choice == "Athletics" and "Athletics" not in picked:
                    picked.append("Athletics")
                    new_player.skills["Athletics"] += 3
                elif choice == "Nature" and "Nature" not in picked:
                    picked.append("Nature")
                    new_player.skills["Nature"] += 3
                elif choice == "Stealth" and "Stealth" not in picked:
                    picked.append("Stealth")
                    new_player.skills["Stealth"] += 3
                elif choice == "Perception" and "Perception" not in picked:
                    picked.append("Perception")
                    new_player.skills["Perception"] += 3
                elif choice == "Survival" and "Survival" not in picked:
                    picked.append("Survival")
                    new_player.skills["Survival"] += 3
                else: print("Invalid option")
            break;
        elif choice == '9':
            new_player.className = "Rogue"
            new_player.hp += randint(1,8) + new_player.con_mod
            prof = ["Light Armor", "Simple Weapons", "Hand Crossbow", "Longsword", "Rapier", "Shortsword"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Dexterity, Intelligence"
            picked = []
            while len(picked) < 4:
                choice = input("Choose four of the following skills to be trained in Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, or Stealth: ")
                if choice == "Acrobatics" and "Acrobatics" not in picked:
                    picked.append("Acrobatics")
                    new_player.skills["Acrobatics"] += 3
                elif choice == "Athletics" and "Athletics" not in picked:
                    picked.append("Athletics")
                    new_player.skills["Athletics"] += 3
                elif choice == "Deception" and "Deception" not in picked:
                    picked.append("Deception")
                    new_player.skills["Deception"] += 3
                elif choice == "Insight" and "Insight" not in picked:
                    picked.append("Insight")
                    new_player.skills["Insight"] += 3
                elif choice == "Intimidation" and "Intimidation" not in picked:
                    picked.append("Intimidation")
                    new_player.skills["Intimidation"] += 3
                elif choice == "Investigation" and "Investigation" not in picked:
                    picked.append("Investigation")
                    new_player.skills["Investigation"] += 3
                elif choice == "Stealth" and "Stealth" not in picked:
                    picked.append("Stealth")
                    new_player.skills["Stealth"] += 3
                elif choice == "Performance" and "Performance" not in picked:
                    picked.append("Performance")
                    new_player.skills["Performance"] += 3
                elif choice == "Sleight of Hand" and "Sleight of Hand" not in picked:
                    picked.append("Sleight of Hand")
                    new_player.skills["Sleight of Hand"] += 3
                elif choice == "Perception" and "Perception" not in picked:
                    picked.append("Perception")
                    new_player.skills["Perception"] += 3
                elif choice == "Survival" and "Survival" not in picked:
                    picked.append("Survival")
                    new_player.skills["Survival"] += 3
                else: print("Invalid option")
            break;
        elif choice == '10':
            new_player.className = "Sorcerer"
            new_player.hp += randint(1,6) + new_player.con_mod
            prof = ["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Constitution, Charisma"
            picked = []
            while len(picked) < 2:
                choice = input("Choose two of the following skills to be trained in Arcana, Deception, Insight, Intimidation, Persuasion, or Religion: ")
                if choice == "Arcana" and "Arcana" not in picked:
                    picked.append("Arcana")
                    new_player.skills["Arcana"] += 3
                elif choice == "Deception" and "Deception" not in picked:
                    picked.append("Deception")
                    new_player.skills["Deception"] += 3
                elif choice == "Insight" and "Insight" not in picked:
                    picked.append("Insight")
                    new_player.skills["Insight"] += 3
                elif choice == "Intimidation" and "Intimidation" not in picked:
                    picked.append("Intimidation")
                    new_player.skills["Intimidation"] += 3
                elif choice == "Persuasion" and "Persuasion" not in picked:
                    picke.append("Persuasion")
                    new_player.skills["Persuasion"] += 3
                elif choice == "Religion" and "Religion" not in picked:
                    picked.append("Religion")
                    new_player.skills["Religion"] += 3
                else: print("Invalid option")
            break;
        elif choice == '11':
            new_player.className = "Warlock"
            new_player.hp += randint(1,8) + new_player.con_mod
            prof = ["Light Armor", "Simple Weapon"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Wisdom, Charisma"
            picked = []
            while len(picked) < 2:
                choice = input("Choose two of the following skills to be trained in Arcana, Deception, History, Intimidation, Investigation, Nature, or Religion: ")
                if choice == "Arcana" and "Arcana" not in picked:
                    picked.append("Arcana")
                    new_player.skills["Arcana"] += 3
                elif choice == "Deception" and "Deception" not in picked:
                    picked.append("Deception")
                    new_player.skills["Deception"] += 3
                elif choice == "History" and "History" not in picked:
                    picked.append("History")
                    new_player.skills["History"] += 3
                elif choice == "Intimidation" and "Intimidation" not in picked:
                    picked.append("Intimidation")
                    new_player.skills["Intimidation"] += 3
                elif choice == "Investigation" and "Investigation" not in picked:
                    picked.append("Investigation")
                    new_player.skills["Investigation"] += 3
                elif choice == "Nature" and "Nature" not in picked:
                    picked.append("Nature")
                    new_player.skills["Nature"] += 3
                elif choice == "Religion" and "Religion" not in picked:
                    picked.append("Religion")
                    new_player.skills["Religion"] += 3
                else: print("Invalid option")
            break;
        elif choice == '12':
            new_player.className = "Wizard"
            new_player.hp += randint(1,6) + new_player.con_mod
            prof = ["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"]
            add_distinct(prof)
            new_player.prof_bonus = 2
            new_player.save = "Intelligence, Wisdom"
            picked = []
            while len(picked) < 2:
                choice = input("Choose two of the following skills to be trained in Arcana, History, Insight, Investigation, Medicine, or Religion: ")
                if choice == "Arcana" and "Arcana" not in picked:
                    picked.append("Arcana")
                    new_player.skills["Arcana"] += 3
                elif choice == "Insight" and "Insight" not in picked:
                    picked.append("Insight")
                    new_player.skills["Insight"] += 3
                elif choice == "History" and "History" not in picked:
                    picked.append("History")
                    new_player.skills["History"] += 3
                elif choice == "Medicine" and "Medicine" not in picked:
                    picked.append("Medicine")
                    new_player.skills["Medicine"] += 3
                elif choice == "Investigation" and "Investigation" not in picked:
                    picked.append("Investigation")
                    new_player.skills["Investigation"] += 3
                elif choice == "Religion" and "Religion" not in picked:
                    picked.append("Religion")
                    new_player.skills["Religion"] += 3
                else: print("Invalid option")
            break;
        else: print("Invalid option")

def eval_mods():
    stats = [new_player.str, new_player.dex, new_player.con, new_player.int, new_player.wis, new_player.cha]
    str_mod = dex_mod = con_mod = int_mod = wis_mod = cha_mod = 0
    mods = [str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod]
    for i in range(6):
        if stats[i] == 1:
            mods[i] = -5
        elif stats[i] == 2 or stats[i] == 3:
            mods[i] = -4
        elif stats[i] == 4 or stats[i] == 5:
            mods[i] = -3
        elif stats[i] == 6 or stats[i] == 7:
            mods[i] = -2
        elif stats[i] == 8 or stats[i] == 9:
            mods[i] = -1
        elif stats[i] == 10 or stats[i] == 11:
            mods[i] = 0
        elif stats[i] == 12 or stats[i] == 13:
            mods[i] = 1
        elif stats[i] == 14 or stats[i] == 15:
            mods[i] = 2
        elif stats[i] == 16 or stats[i] == 17:
            mods[i] = 3
        elif stats[i] == 18 or stats[i] == 19:
            mods[i] = 4
        elif stats[i] == 20 or stats[i] == 21:
            mods[i] = 5
        elif stats[i] == 22 or stats[i] == 23:
            mods[i] = 6    
        elif stats[i] == 24 or stats[i] == 25:
            mods[i] = 8
        elif stats[i] == 26 or stats[i] == 27:
            mods[i] = 9
        else:
            mods[i] = 10
                
    new_player.str_mod = mods[0]
    new_player.dex_mod = mods[1]
    new_player.con_mod = mods[2]
    new_player.int_mod = mods[3]
    new_player.wis_mod = mods[4]
    new_player.cha_mod = mods[5]

    new_player.init = new_player.dex_mod
    
    new_player.skills["Acrobatics"] = new_player.dex_mod
    new_player.skills["Animal Handling"] = new_player.wis_mod
    new_player.skills["Arcana"] = new_player.int_mod
    new_player.skills["Athletics"] = new_player.str_mod
    new_player.skills["Deception"] = new_player.cha_mod
    new_player.skills["History"] = new_player.int_mod
    new_player.skills["Insight"] = new_player.wis_mod
    new_player.skills["Intimidation"] = new_player.cha_mod
    new_player.skills["Investigation"] = new_player.int_mod
    new_player.skills["Medicine"] = new_player.wis_mod
    new_player.skills["Nature"] = new_player.int_mod
    new_player.skills["Perception"] = new_player.wis_mod
    new_player.skills["Performance"] = new_player.cha_mod
    new_player.skills["Persuasion"] = new_player.cha_mod
    new_player.skills["Religion"] = new_player.int_mod
    new_player.skills["Sleight of Hand"] = new_player.dex_mod
    new_player.skills["Stealth"] = new_player.dex_mod
    new_player.skills["Survival"] = new_player.wis_mod
    
def print_player(player):
    print("")
    print("Name: " + player.name)
    print("Race: " + player.race)
    print("Class: " + player.className)
    print("Hit Points: " + str(player.hp))
    print("Strength: " + str(player.str))
    print("Dexterity: " + str(player.dex))
    print("Constitution: " + str(player.con))
    print("Intelligence: " + str(player.int))
    print("Wisdom: " + str(player.wis))
    print("Charisma: " + str(player.cha))
    print("Strength Modifier: " + str(player.str_mod))
    print("Dexterity Modifier: " + str(player.dex_mod))
    print("Constitution Modifier: " + str(player.con_mod))
    print("Intelligence Modifier: " + str(player.int_mod))
    print("Wisdom Modifier: " + str(player.wis_mod))
    print("Charisma Modifier: " + str(player.cha_mod))
    print("Saving Throws: " + player.save)
    print("Speed: " + str(player.speed))
    print("Initiative: " + str(player.init))
    print("Skills" + str(player.skills))
    print("Proficieny Bonus: " + str(player.prof_bonus))
    print("Proficienies: " + str(player.prof))
    print("Recommended Alignment: " + str(player.rec_alignment))
    print("Traits: " + str(player.traits))
    print("Languages: " + str(player.lang))
    print("Size: " + str(player.size))

def main():
    print("Welcome to the basic Dungeons and Dragons 5e character generator!")
    print("This program will walk your through the basic character creation process of a dnungeons and drangons 5th edition character!")
    new_player.name = input("What is your new character's name: ")
    print(new_player.name)
    abil_menu()
    race_menu()
    eval_mods()
    class_menu()
    print_player(new_player)
    print("Make sure to look at the pages referenced to get more specific abilities, equipment, etc. This is mostly to just draft your stats quickly!")

new_player = Player()

if __name__ == "__main__":
    main()