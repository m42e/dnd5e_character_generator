#TODO skill versatility, proficeincy flag, and size

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
    new_player.str = input("What is your strength: ")
    new_player.dex = input("What is your dexterity: ")
    new_player.con = input("What is your constitution: ")
    new_player.int = input("What is your intelligence: ")
    new_player.wis = input("What is your wisdom: ")
    new_player.cha = input("What is your charisma: ")

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
    print("\nA brief explanation of ability scores in terms of a tomato\nStrength is your ability to crush a tomato\nDexterity is the ability to dodge a tomato thrown at you\nConstitution is the ability to eat a rotten tomato and not get sick\nIntelligence is knowing a tomato is a fruit\nWisdom is knowing not to put a tomato in a fruit salad\nCharisma is being able to sell a tomato based fruit salad\nFor more information see Pg 14")
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
        choice = input("What langauge would you like to add to your character Dwarvish, Elvish, Giant, Gnomish, Goblin, Halfling, Orc, Abyssal, Celestial, Draconic, Deep Speech, Infernal, Primordial, Undercommon, Sylvan, Druidic").upper()
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
                    new_lang = new_lang()
                    while True:
                        if new_lang in new_player.lang:
                            print("Your character already knows that language, please choose another")
                            new_lang = new_lang()
                        else:
                            new_player.lang += new_lang
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
            new_lang = new_lang()
            new_player.lang += ["Common",new_lang]
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
            while True:
                if new_lang in new_player.lang:
                    print("Your character already knows that language, please choose another")
                    new_lang = new_lang()
                else:
                    new_player.lang += new_lang
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
            new_player.languages += ["Common","Orc"]
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

def main():
    print("Welcome to the basic Dungeons and Dragons 5e character generator!")
    print("This program will walk your through the basic character creation process of a dnungeons and drangons 5th edition character!")
    new_player.name = input("What is your new character's name: ")
    print(new_player.name)
    abil_menu()
    race_menu()

new_player = Player()

if __name__ == "__main__":
    main()